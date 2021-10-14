


from rdflib import Graph, URIRef, Literal, RDF
from rdflib.namespace import Namespace
import pandas as pd

sio = Namespace('http://semanticscience.org/')
esgreen = Namespace('https://w3id.org/esgreen/')

g = Graph()
g.bind('sio', sio)
g.bind('esgreen', esgreen)


def createAttr(g, s, p, o, extra = {}):
    """Create reified association"""
    s_uri = str(s).replace(' ', '')
    o = str(o).replace(' ', '')
    s_uri = esgreen[s_uri]
    o = esgreen[o]

    associationUri = URIRef(str(s_uri) + '/location')

    g.add((s_uri, sio['title'], Literal(s)))
    g.add((s_uri, sio['hasAttribute'], associationUri))
    g.add((associationUri, RDF.type, p))
    g.add((associationUri, sio['hasValue'], o))

    # g.add((s, p, o))
    return g

# pd.read_csv()
df = pd.read_csv('data/inputs/ArboladoParquesHistoricoSingularesForestales_2020.csv', sep = ';') 

for index, row in df.iterrows():
    g = createAttr(g, 
        s=row['ESPECIE'], 
        p=sio['Location'], 
        o=row['PARQUE'], 
        extra={sio['hasCount']: df['UNIDADES 2020']}
    )


# print(g.serialize(format='turtle'))
g.serialize('rdflib-output.ttl', format='turtle')