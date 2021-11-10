

# Import Libraries
from rdflib import Graph, URIRef, Literal, RDF, XSD, RDFS #basic RDF handling
from rdflib.namespace import Namespace #common namespace
import pandas as pd #for handling csv and csv contents

# Define graph 'g' and namespaces
sio = Namespace('http://semanticscience.org/resource/')
esgreen = Namespace('https://w3id.org/esgreen/')
obo = Namespace('http://purl.obolibratory.org/obo/')

g = Graph()
g.bind('sio', sio)
g.bind('esgreen', esgreen)

def prepareUri(uri):
    return esgreen + str(uri).replace(' ', '_').replace('"', '').lower()


file_dates = [ '2019', '2020' ]


for file_date in file_dates:
    # Read in the csv file
    df = pd.read_csv(f'data/inputs/preprocessing//MasasParquesHistoricoSingularesForestales_{file_date}.csv', sep = ';') 
    if file_date == '2020':
        df.rename(columns={'superficie_ocupada__(m2)_':'superficie_ocupada_(m2)'}, inplace=True)
        surface_col = 'superficie_ocupada_(m2)'
        especie_col = 'especie_predominante'
        count_col = 'unidades_' + file_date#.replace('_', '')   
    else:
        file_date = file_date.replace('_', '')
        count_col = 'unidades_' + file_date#.replace('_', '')
        especie_col = 'especie_predominante'  
        surface_col = 'superficie_ocupada_(m2)'  

    # Iterate dataframe and generate RDF triples
    for index, row in df.iterrows():

        park_uri = URIRef(prepareUri(row['parque']))
        specie_uri = URIRef(prepareUri(row[especie_col]))

        collection_uri = URIRef(prepareUri(f"collection-{row[especie_col]}-{row['parque']}"))
        count_uri = URIRef(prepareUri(f"count-{file_date}-{row[especie_col]}-{row['parque']}"))
        surface_uri = URIRef(prepareUri(f"Total-surface-{file_date}-{row[especie_col]}-{row['parque']}"))
        
        g.add((park_uri, RDF.type, sio.site))
        g.add((park_uri, RDFS.label, Literal(str(row['parque']).lower())))

        g.add((collection_uri, RDF.type, sio.Collection))
        g.add((collection_uri, sio.hasMember, specie_uri))
        g.add((collection_uri, sio.hasAttribute, count_uri))

        g.add((count_uri, RDF.type, sio.MemberCount))
        g.add((surface_uri, RDF.type, sio.SurfaceArea))
        g.add((count_uri, sio.hasValue, Literal(row[count_col], datatype=XSD.integer)))
        g.add((count_uri, sio.hasUnit, obo.UO_0000189))
        g.add((surface_uri, sio.hasValue, Literal(row[surface_col], datatype=XSD.Float)))
        g.add((surface_uri, sio.hasUnit, obo.UO_0000082)) #mts square
        g.add((count_uri, sio.measuredAt, Literal(file_date, datatype=XSD.integer)))
        g.add((surface_uri, sio.measuredAt, Literal(file_date, datatype=XSD.integer)))

        g.add((specie_uri, RDF.type, sio.Specie))
        g.add((specie_uri, RDFS.label, Literal(str(row[especie_col]).lower())))


        # g = createAttr(g, 
        #     predType=sio['memberCount'], 
        #     subject=row[especie_col], 
        #     obj=row['PARQUE'], 
        #     extra={'memberCount': row['UNIDADES 2020']}
        # )


## Example with columns header
# :PARQUE rdf:type sio:Site .
# :PARQUE sio:isLocatedIn District .
# :PARQUE sio:contains :collection-of-ESPECIE .

# :collection-of-ESPECIE rdf:type sio:Collection .
# :collection-of-ESPECIE sio:hasMember :ESPECIE .
# :collection-of-ESPECIE sio:has-attribute :UNIDADES .
# :collection-of-ESPECIE sio:has-surface :SUPERFICIE OCUPADA (m2) .
# :SUPERFICIE OCUPADA (m2) a sio:SurfaceArea .
# :UNIDADES a sio:memberCount .
# :UNIDADES sio:has-value "UNIDADES YEAR"

# :ESPECIE a :habitatSpecies.
# :ESPECIE sio:has-unique-identifier :ESPECIE-code .
# :ESPECIE-Code sio:has-value "G3.74" .

# MasasParquesHistoricoSingularesForestales_YYYY.csv
######## Turtle syntax ########

# :Parques-Madrid-Rio rdf:type :Park .
# Park sio: isLocatedIn District .
# :Parques-Madrid-Rio sio:contains :collection-of-pinus-alepensis .
# :collection-of-pinus-alepensis a sio:Collection .
# :collection-of-pinus-alepensis sio:hasMember :pinus-alepensis .
# :pinus-alepensis a :habitatSpecies.
# :pinus-alepensis sio: has-unique-indentifier :EUNIS-code .
# :EUNIS-Code sio:has-value "G3.74" .
# :collection-of-pinus-alepensis sio:has-attribute :parques-madrid-rio_sa .
# ::parques-madrid-rio_sa a sio:SurfaceArea.
# ::parques-madrid-rio_sa sio:has-value "92970.17" .
# :collection-of-pinus-alepensis sio:has-attribute :parques-madrid-rio_count .
# ::parques-madrid-rio_count a sio:memberCount.
# ::parques-madrid-rio_count sio:has-value "2811" .




outputfile = 'outputs/rdflib-output5.ttl'
g.serialize(outputfile, format='turtle')
print(f'**************************finished********************************* file in:' + outputfile)
#g.serialize('outputs/rdflib-output3.ttl', format='turtle')