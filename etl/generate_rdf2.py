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


file_dates = [ '_2019', '_2020', '_2017' ]


for file_date in file_dates:
    # Read in the csv file
    df = pd.read_csv(f'data/inputs/preprocessing/ArboladoZonasVerdesDistritosCalles{file_date}.csv', sep = ';') 
    file_date = file_date.replace('_', '')
    print(file_date)
    if file_date == '2017':
        especie_col = 'especie'
        count_col = 'unidades'
        district_col = 'distrito'
    else:
        #file_date = file_date.replace('_', '')
        count_col = 'n_unidades'
        especie_col = 'nombre_especie'
        district_col = 'nombre_distrito'
        
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

        district_uri = URIRef(prepareUri(row[district_col]))
        specie_uri = URIRef(prepareUri(row[especie_col]))
        wiki_uri = URIRef(prepareUriWiki(str(row[especie_col]).capitalize()))

        collection_uri = URIRef(prepareUri(f"collection-{row[especie_col]}-{row[district_col]}"))
        count_uri = URIRef(prepareUri(f"count-{file_date}-{row[especie_col]}-{row[district_col]}"))
        
        g.add((district_uri, RDF.type, sio.SpatialRegion))
        g.add((district_uri, RDFS.label, Literal(str(row[district_col]).lower())))

        g.add((collection_uri, RDF.type, sio.Collection))
        g.add((collection_uri, sio.hasMember, specie_uri))
        g.add((collection_uri, sio.hasAttribute, count_uri))

        g.add((count_uri, RDF.type, sio.MemberCount))
        g.add((count_uri, sio.hasValue, Literal(row[count_col], datatype=XSD.integer)))
        g.add((count_uri, sio.hasUnit, obo.UO_0000189))
        g.add((count_uri, sio.measuredAt, Literal(file_date, datatype=XSD.date)))

        g.add((specie_uri, RDF.type, sio.Specie))
        g.add((specie_uri, RDFS.label, Literal(str(row[especie_col]).lower())))
        g.add((specie_uri, RDFS.seeAlso, wiki_uri))


        # g = createAttr(g, 
        #     predType=sio['memberCount'], 
        #     subject=row[especie_col], 
        #     obj=row['PARQUE'], 
        #     extra={'memberCount': row['UNIDADES 2020']}
        # )


# print(g.serialize(format='turtle'))
outputfile = 'outputs/rdflib-output2.ttl'
g.serialize(outputfile, format='turtle')
print(f'finished....' + outputfile)