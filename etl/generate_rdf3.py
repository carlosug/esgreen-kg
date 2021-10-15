

# Import Libraries
from rdflib import Graph, URIRef, Literal, RDF #basic RDF handling
from rdflib.namespace import Namespace #common namespace
import pandas as pd #for handling csv and csv contents

# Import Libraries
from rdflib import Graph, URIRef, Literal, RDF, XSD, RDFS #basic RDF handling
from rdflib.namespace import Namespace #common namespace
import pandas as pd #for handling csv and csv contents

# Define graph 'g' and namespaces
sio = Namespace('http://semanticscience.org/resource/')
esgreen = Namespace('https://w3id.org/esgreen/')

g = Graph()
g.bind('sio', sio)
g.bind('esgreen', esgreen)

def prepareUri(uri):
    return esgreen + str(uri).replace(' ', '_').replace('"', '').lower()


file_dates = [ '_2019', '_2020']



for file_date in file_dates:
    # Read in the csv file
    df = pd.read_csv(f'data/inputs/ArboladoParquesHistoricoSingularesForestales{file_date}.csv', sep = ';') 
    
    # #if file_date == '2017':
    #     count_col = 'N� de ejemplares'
    #     especie_col = 'Especie'
    # else:
    #     file_date = file_date.replace('_', '')
    #     count_col = 'UNIDADES ' + file_date.replace('_', '')
    #     especie_col = 'ESPECIE'

    # Create the triples and add them to graph 'g'
    # def createAttr(g, predType, subject, obj, extra = {}):
    #     """Create reified association"""
    #     s_uri = str(subject).replace(' ', '')
    #     obj = str(obj).replace(' ', '')
    #     s_uri = esgreen[s_uri]
    #     obj = esgreen[obj]

    #     associationUri = URIRef(str(s_uri) + '/location')

    #     g.add((s_uri, sio['ScientificName'], Literal(subject)))
    #     g.add((s_uri, sio['hasAttribute'], associationUri))
    #     g.add((associationUri, RDF.type, predType))
    #     g.add((associationUri, sio['hasValue'], obj))

    #     for extraProp, extraValue in extra.items():
    #         if str(extraValue).startswith('http://') or str(extraValue).startswith('https://'):
    #             g.add((associationUri, sio[extraProp], URIRef(extraValue)))
    #         else: 
    #             g.add((associationUri, sio[extraProp], Literal(extraValue)))   
    #     return g
    columns = df.columns
    # Iterate dataframe and generate RDF triples
    for index, row in df.iterrows():

        park_uri = URIRef(prepareUri(row['PARQUE']))
        #specie_uri = URIRef(prepareUri(row[especie_col]))

        STATUS_uri = URIRef(prepareUri(f"collectionofTreesIn-{columns}-{row['PARQUE']}"))
        count_uri = URIRef(prepareUri(f"count-{file_date}-{row[columns]}-{row['PARQUE']}"))
        
        g.add((park_uri, RDF.type, sio.site))
        g.add((park_uri, RDFS.label, Literal(str(row['PARQUE']).lower())))

        g.add((STATUS_uri, RDF.type, sio.Collection))
        g.add((STATUS_uri, sio.hasAttribute, count_uri))
        
        g.add((count_uri, RDF.type, sio.MemberCount))
        g.add((count_uri, sio.hasValue, Literal(row[columns], datatype=XSD.integer)))
        g.add((count_uri, sio.measuredAt, Literal(file_date, datatype=XSD.integer)))

        # g.add((specie_uri, RDF.type, sio.Specie))
        # g.add((specie_uri, RDFS.label, Literal(str(row[especie_col]).lower())))


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
# :UNIDADES a sio:memberCount .
# :UNIDADES sio:has-value "UNIDADES YEAR"

# :ESPECIE a :habitatSpecies.
# :ESPECIE sio:has-unique-identifier :ESPECIE-code .
# :ESPECIE-Code sio:has-value "G3.74" .


## Example with columns header
# :PARQUE rdf:type sio:Site .
# :PARQUE sio: isLocatedIn District .
# :PARQUE sio:contains :collection-of-ESPECIE-STATUS .

# :collection-of-ESPECIE-STATUS rdf:type sio:Collection .
# :collection-of-trees sio:hasAttribute :age .
# :age a :subClassOf sio:dimensional-quantity .
# :age sio: has-label :lifeCycleInfo .
# :lifeCycleInfo sio:has-value "New" .
# :lifeCycleInfo a sio:memberCount .
# :cph_count sio:has-value "8" .  
# :collection-of-trees sio:hasAttribute : averageHeight-Parque-Madrid-Rio .
# :averageHeight a sio:mean .
# :averageHeight-Parque-Madrid-Rio sio: has-value "5.99" .
# :collection-of-trees sio:hasAttribute :circumference-Parque-Madrid-Rio .
# :circumference-Parque-Madrid-Rio a sio:dimensional-quantity .
# :circumference-Parque-Madrid-Rio sio: has-value "32.49" .

## Example with values
# Estado_arbolado_ParquesHistoricoSingularesForestales_YYYY.csv
######## Turtle syntax ########

# :Parque-Madrid-Rio rdf:type :Park .
# Park sio: isLocatedIn District .
# :Parques-Madrid-Rio sio:contains :collection-of-trees .
# :collection-of-trees a sio:Collection .
# :collection-of-trees sio:hasAttribute :age .
# :age a :subClassOf sio:dimensional-quantity .
# :age sio: has-label :lifeCycleInfo .
# :lifeCycleInfo sio:has-value "New" .
# :lifeCycleInfo a sio:memberCount .
# :cph_count sio:has-value "8" .  
# :collection-of-trees sio:hasAttribute : averageHeight-Parque-Madrid-Rio .
# :averageHeight a sio:mean .
# :averageHeight-Parque-Madrid-Rio sio: has-value "5.99" .
# :collection-of-trees sio:hasAttribute :circumference-Parque-Madrid-Rio .
# :circumference-Parque-Madrid-Rio a sio:dimensional-quantity .
# :circumference-Parque-Madrid-Rio sio: has-value "32.49" .




# print(g.serialize(format='turtle'))
g.serialize('outputs/rdflib-output3.ttl', format='turtle')