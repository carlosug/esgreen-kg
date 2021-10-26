

# Import Libraries
from rdflib import Graph, URIRef, Literal, RDF, XSD, RDFS #basic RDF handling
from rdflib.namespace import Namespace #common namespace
import pandas as pd #for handling csv and csv contents
import unicodedata
import re

# Define graph 'g' and namespaces
sio = Namespace('http://semanticscience.org/resource/')
esgreen = Namespace('https://w3id.org/esgreen/')

g = Graph()
g.bind('sio', sio)
g.bind('esgreen', esgreen)

def prepareUri(uri):
    return esgreen + str(uri).replace(' ', '_').replace('"', '').lower()
    



file_dates = [ '_2019', '_2020', '2017' ]
pattern = r"\n^;Total:;(.*?)$"

pattern = r"^;Total:;(.*?)$"
pattern = "^;Total:;(.*?)$"


for file_date in file_dates:
    # Read in the csv file
    df = pd.read_csv(f'data/inputs/ArboladoParquesHistoricoSingularesForestales{file_date}.csv', sep = ';')



    # data cleaning
    df.columns = df.columns.str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')] # remove unnamed cols
    df.columns = df.columns.str.replace(" ", "_")

    #print(df.tail(8))
    if file_date == '2017':
        df['N_de_ejemplares'] = df['N_de_ejemplares'].apply(str).str.replace(u"�", "u")     
        count_col = 'N_de_ejemplares'
        especie_col = 'Especie'
        #print(f'if',count_col, especie_col, file_date)
    else:
        file_date = file_date.replace('_', '')
        count_col = 'UNIDADES_' + file_date
        especie_col = 'ESPECIE'
        #print(f'else',count_col, especie_col, file_date)

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

    # Iterate dataframe and generate RDF triples
    for index, row in df.iterrows():
        park_uri = URIRef(prepareUri(row['PARQUE']))
        specie_uri = URIRef(prepareUri(row[especie_col]))

        collection_uri = URIRef(prepareUri(f"collection-{row[especie_col]}-{row['PARQUE']}"))
        count_uri = URIRef(prepareUri(f"count-{file_date}-{row[especie_col]}-{row['PARQUE']}"))
        
        g.add((park_uri, RDF.type, sio.site))
        g.add((park_uri, RDFS.label, Literal(str(row['PARQUE']).lower())))

        g.add((collection_uri, RDF.type, sio.Collection))
        g.add((collection_uri, sio.hasMember, specie_uri))
        g.add((collection_uri, sio.hasAttribute, count_uri))

        g.add((count_uri, RDF.type, sio.MemberCount))
        g.add((count_uri, sio.hasValue, Literal(row[count_col], datatype=XSD.integer)))
        g.add((count_uri, sio.measuredAt, Literal(file_date, datatype=XSD.integer)))

        g.add((specie_uri, RDF.type, sio.Specie))
        g.add((specie_uri, RDFS.label, Literal(str(row[especie_col]).lower())))


        # g = createAttr(g, 
        #     predType=sio['memberCount'], 
        #     subject=row[especie_col], 
        #     obj=row['PARQUE'], 
        #     extra={'memberCount': row['UNIDADES 2020']}
        # )


# ## Example with columns header
# # :PARQUE rdf:type sio:Site .
# # :PARQUE sio:isLocatedIn District .
# # :PARQUE sio:contains :collection-of-ESPECIE .

# # :collection-of-ESPECIE rdf:type sio:Collection .
# # :collection-of-ESPECIE sio:hasMember :ESPECIE .
# # :collection-of-ESPECIE sio:has-attribute :UNIDADES .
# # :UNIDADES a sio:memberCount .
# # :UNIDADES sio:has-value "UNIDADES YEAR"

# # :ESPECIE a :habitatSpecies.
# # :ESPECIE sio:has-unique-identifier :ESPECIE-code .
# # :ESPECIE-Code sio:has-value "G3.74" .



# ## Example with values
# # :Jardines-del-buen-retiro rdf:type :Park .
# # Park sio: isLocatedIn District .
# # :Jardines-del-buen-retiro sio:contains :collection-of-aesculus-hippocastanum .
# # :collection-of-aesculus-hippocastanum a sio:Collection .
# # :collection-of-aesculus-hippocastanum sio:hasMember :aesculus-hippocastanum .
# # :aesculus-hippocastanum a :habitatSpecies.
# # :aesculus-hippocastanum sio: has-unique-indentifier :EUNIS-code .
# # :EUNIS-Code sio:has-value "G3.74" .
# # :collection-of-aesculus-hippocastanum sio:has-attribute :UNIDADES .
# # :UNIDADES a sio:memberCount .
# # :UNIDADES sio:has-value "UNIDADES YEAR"




# print(g.serialize(format='turtle'))
g.serialize('outputs/rdflib-output.ttl', format='turtle')
print('finished....')