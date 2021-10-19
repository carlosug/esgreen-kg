

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
    return str(esgreen) + str(uri).replace(' ', '_').replace('"', '').lower()


file_dates = ['_2017', '_2019', '_2020']

for file_date in file_dates:
    # Read in the csv file
    df = pd.read_csv(f'data/inputs/Estado_arbolado_ParquesHistoricoSingularesForestales{file_date}.csv', sep = ';')   
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')] # remove unnamed cols
    df.columns = df.columns.str.replace(" ", "_")
    print(df.columns)
    # cols = df.columns.to_list()
    #statuses = ['Recien-plantado-y-no-consolidado','Joven', 'Maduro', 'Viejo', 'Otros']
    if file_date == '2017':
        count_col = 'N� de ejemplares'
        statuses = ['Joven', 'Maduro', 'Viejo', 'Otros']
    else:
        file_date = file_date.replace('_', '')
        count_col = 'UNIDADES ' + file_date.replace('_', '')
        statuses = ['Joven', 'Maduro', 'Viejo', 'Otros']

#     # print(cols)
#     # for (idx, row) in df.iterrows():
#     #     cols = df.columns
#     #     #cols = cols.replace('�', '')
#     #     #print(cols)
    
    # Iterate dataframe and generate RDF triples
    for index, row in df.iterrows():
        park_uri = URIRef(prepareUri(row['PARQUE']))

        status_uris = {}
        # for age_status in statuses:
        #     status_uris[age_status] = URIRef(prepareUri(age_status))
        print(status_uris)
        collection_uri = URIRef(prepareUri(f"collection-of-trees-in-{row['PARQUE']}"))
        count_uri = URIRef(prepareUri(f"count-{file_date}-{row['PARQUE']}"))
        
        g.add((park_uri, RDF.type, sio.site))
        g.add((park_uri, RDFS.label, Literal(str(row['PARQUE']).lower())))
        g.add((collection_uri, RDF.type, sio.Collection))
        print(statuses)
        for age_status in statuses:
            print('toto')
            # age_status_uri = URIRef(prepareUri(age_status))
            age_status_uri = URIRef(str(collection_uri) + '-' + age_status.lower())
            print(age_status_uri)
            g.add((age_status_uri, RDF.type, sio.LifeStatus))
            g.add((age_status_uri, sio.hasQuality, Literal(age_status)))
            g.add((age_status_uri, sio.hasAttribute, Literal(row[age_status], datatype=XSD.integer)))

        g.add((count_uri, RDF.type, sio.MemberCount))
        g.add((count_uri, sio.hasValue, Literal(row[age_status], datatype=XSD.integer)))
        g.add((count_uri, sio.measuredAt, Literal(file_date, datatype=XSD.integer)))

        # g.add((status_uri, RDF.type, sio.LifeStatus))
        # g.add((status_uri, RDFS.label, Literal(str(row[age_status]).lower())))



# print(g.serialize(format='turtle'))
g.serialize('outputs/rdflib-output-3.ttl', format='turtle')



# # # ## Example with columns header
# # # # :PARQUE rdf:type sio:Site .
# # # # :PARQUE sio:contains :collection-of-ESPECIE-STATUS .
# # # # :collection-of-ESPECIE-STATUS rdf:type sio:Collection .
# # # # :collection-of-trees sio:hasAttribute :age .
# # # # :age a :subClassOf sio:dimensional-quantity .
# # # # :age sio: has-label :lifeCycleInfo .
# # # # :lifeCycleInfo sio:has-label "Recien plantado y no consolidado" .
# # # # :Recien plantado y no consolidado a sio:memberCount .
# # # # :membercount sio:has-value "Recien plantado y no consolidado" .
# # # # :lifeCycleInfo sio:has-label "Recien plantado y no consolidado" .
# # # # :Recien plantado y no consolidado a sio:memberCount .
# # # # :membercount sio:has-value "Recien plantado y no consolidado" .
# # # # :lifeCycleInfo sio:has-label "Joven" .
# # # # :Joven a sio:memberCount .
# # # # :membercount sio:has-value "Joven" .  
# # # # :collection-of-trees sio:hasAttribute : Maduro .
# # # # :Maduro a sio:mean .
# # # # :Maduro sio: has-value "Maduro" .
# # # # :collection-of-trees sio:hasAttribute : Viejo .
# # # # :Viejo a sio:mean .
# # # # :Viejo sio: has-value "Viejo" .

# # # ## Example with values
# # # # Estado_arbolado_ParquesHistoricoSingularesForestales_YYYY.csv
# # # ######## Turtle syntax ########

# # # # :Parque-Madrid-Rio rdf:type :Park .
# # # # Park sio: isLocatedIn District .
# # # # :Parques-Madrid-Rio sio:contains :collection-of-trees .
# # # # :collection-of-trees a sio:Collection .
# # # # :collection-of-trees sio:hasAttribute :age .
# # # # :age a :subClassOf sio:dimensional-quantity .
# # # # :age sio: has-label :lifeCycleInfo .
# # # # :lifeCycleInfo sio:has-value "New" .
# # # # :lifeCycleInfo a sio:memberCount .
# # # # :cph_count sio:has-value "8" .  
# # # # :collection-of-trees sio:hasAttribute : averageHeight-Parque-Madrid-Rio .
# # # # :averageHeight a sio:mean .
# # # # :averageHeight-Parque-Madrid-Rio sio: has-value "5.99" .
# # # # :collection-of-trees sio:hasAttribute :circumference-Parque-Madrid-Rio .
# # # # :circumference-Parque-Madrid-Rio a sio:dimensional-quantity .
# # # # :circumference-Parque-Madrid-Rio sio: has-value "32.49" .




# # # # print(g.serialize(format='turtle'))
# # # g.serialize('outputs/rdflib-output3.ttl', format='turtle')