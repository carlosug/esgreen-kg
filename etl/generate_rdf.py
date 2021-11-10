

# Import Libraries
from rdflib import Graph, URIRef, Literal, RDF, XSD, RDFS #basic RDF handling
from rdflib.namespace import Namespace #common namespace
import pandas as pd #for handling csv and csv contents
import unicodedata
import re
import fileinput
import csv


# Define graph 'g' and namespaces
sio = Namespace('http://semanticscience.org/resource/')
esgreen = Namespace('https://w3id.org/esgreen/')
obo = Namespace('http://purl.obolibrary.org/obo/')
#eol = Namespace('https://eol.org/pages/')
wiki = Namespace('http://en.wikipedia.org/wiki/')

g = Graph()
g.bind('sio', sio)
g.bind('esgreen', esgreen)

def prepareUri(uri):
    return esgreen + str(uri).replace(' ', '_').replace('"', '').lower()

def prepareUriWiki(uri):
    return wiki + str(uri).replace(' ', '_').replace('"', '')

# def prepareUriEOL(uri):
#     return eol + str(uri).replace(' ', '_').replace('"', '').lower()



file_dates = [ '_2019', '_2020', '2017' ]


for file_date in file_dates:
    # Read in the csv file
    df = pd.read_csv(f'data/inputs/preprocessing/ArboladoParquesHistoricoSingularesForestales{file_date}.csv', sep = ';')
    # data cleaning
    #df = df.loc[:, ~df.columns.str.contains('^Unnamed')] # remove unnamed cols

    #print(df.tail(8))
    if file_date == '2017':
        count_col = 'n_de_ejemplares'
        especie_col = 'especie'
        #print(f'if',count_col, especie_col, file_date)
    else:
        file_date = file_date.replace('_', '')
        count_col = 'unidades_' + file_date
        especie_col = 'especie'

    # list_especies = df[especie_col]
    # res_list = []
    # for especie in list_especies:
    #     if especie not in res_list:
    #         res_list.append(especie)
    
    # print('Unique especies of the list using append:')
    # for especie in res_list:
    #     print(especie)
    # print(len(res_list))
        #print(f'else',count_col, especie_col, file_date)
    # for index, row in df.iterrows():
    #     print (row[especie_col].capitalize())

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
        #a= str((row[especie_col]).capitalize())
        park_uri = URIRef(prepareUri(row['parque']))
        specie_uri = URIRef(prepareUri(row[especie_col]))
        wiki_uri = URIRef(prepareUriWiki(str(row[especie_col]).capitalize()))
        #print(wiki_uri)
        # eol_uri = URIRef(prepareUriEOL(row[especie_col]))

        collection_uri = URIRef(prepareUri(f"collection-{row[especie_col]}-{row['parque']}"))
        count_uri = URIRef(prepareUri(f"count-{file_date}-{row[especie_col]}-{row['parque']}"))
        
        g.add((park_uri, RDF.type, sio.site))
        g.add((park_uri, RDFS.label, Literal(str(row['parque']).lower())))
        #g.add(COORDINATES)

        g.add((collection_uri, RDF.type, sio.Collection))
        # to add same as https://schema.org/Collection
        g.add((collection_uri, sio.hasMember, specie_uri))
        g.add((specie_uri, RDF.type, obo.FLOPO_0900033))
        g.add((collection_uri, sio.hasAttribute, count_uri))

        g.add((count_uri, RDF.type, sio.MemberCount))
        g.add((count_uri, sio.hasValue, Literal(row[count_col], datatype=XSD.integer)))
        g.add((count_uri, sio.hasUnit, obo.UO_0000189)) # dimensionless unit
        g.add((count_uri, sio.measuredAt, Literal(file_date, datatype=XSD.date)))

        g.add((specie_uri, RDF.type, sio.Specie))
        #g.add((wiki_uri, RDF.type, sio.Specie))
        g.add((specie_uri, RDFS.label, Literal(str(row[especie_col]).lower())))
        # to add: especie sio:UniqueIdentifier :ESPECIE-code .
        g.add((specie_uri, RDFS.seeAlso, wiki_uri))


        # g = createAttr(g, 
        #     predType=sio['memberCount'], 
        #     subject=row[especie_col], 
        #     obj=row['PARQUE'], 
        #     extra={'memberCount': row['UNIDADES 2020']}
        # )


# ## Example with columns header
# # :parque rdf:type sio:Site .
# # :parque sio:isLocatedIn District .
# # :parque sio:contains :collection-of-especie .

# # :collection-of-especie rdf:type sio:Collection .
# # :collection-of-especie sio:hasMember :especie .
# # :collection-of-especie sio:has-attribute :unidades .
# # :unidades a sio:memberCount .
# # :unidades sio:has-value "unidades_year"
# # :unidades sio:has-unit obo:UO_0000009 .

# # :especie a :habitatSpecies.
# # :especie sio:has-unique-identifier :ESPECIE-code .
# # :especie-Code sio:has-value "G3.74" .



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
outputfile = 'outputs/rdflib-output.ttl'
g.serialize(outputfile, format='turtle')
print(f'finished....' + outputfile)