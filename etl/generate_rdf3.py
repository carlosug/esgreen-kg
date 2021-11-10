

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
obo = Namespace('http://purl.obolibratory.org/obo/')
#ppo = Namespace('http://purl.obolibratory.org/ppo/')

g = Graph()
g.bind('sio', sio)
g.bind('esgreen', esgreen)

def prepareUri(uri):
    return str(esgreen) + str(uri).replace(' ', '_').replace('"', '').lower()


file_dates = ['2017', '2018', '2019', '2020']

for file_date in file_dates:
    # Read in the csv file
    df = pd.read_csv(f'data/inputs/preprocessing/EstadoParquesHistoricoSingularesForestales_{file_date}.csv', sep = ';')
    # file_date = file_date.replace('_', '')   
    # df = df.loc[:, ~df.columns.str.contains('^Unnamed')] # remove unnamed cols
    # df.columns = df.columns.str.replace(" ", "_")
    #print('before.....',df.columns)
    # cols = df.columns.to_list()
    #statuses = ['Recien-plantado-y-no-consolidado','Joven', 'Maduro', 'Viejo', 'Otros']
    if file_date == '2017':
        # df.columns = ['parque', 'total_arboles', 'altura_media', 'perimetro_medio_(cm)', 'recien_plantado_y_no_consolidado', 'joven', 'maduro', 'viejo', 'otros']
        #for col in df.columns:
        df.rename(columns={'recien_plantado':'recien_plantado_y_no_consolidado', 'altura_media':'altura_promedio_(m)', 'perimetro_medio': 'perimetro_promedio_(cm)'}, inplace=True)
        stats_col = ['altura_promedio_(m)','perimetro_promedio_(cm)']
        statuses = ['recien_plantado_y_no_consolidado','joven', 'maduro', 'viejo', 'otros']
        #print(statuses)
       # stats_col = 'Altura_media'
    #print(file_date, df)
    else:
        stats_col = ['altura_promedio_(m)','perimetro_promedio_(cm)']
        statuses = ['recien_plantado_y_no_consolidado','joven', 'maduro', 'viejo', 'otros']
        print(file_date, df.columns)
    print(f'after',df.columns)
#     # print(cols)
#     # for (idx, row) in df.iterrows():
#     #     cols = df.columns
#     #     #cols = cols.replace('�', '')
#     #     #print(cols)
    
    ### Iterate dataframe and generate RDF triples
    for index, row in df.iterrows():
        park_uri = URIRef(prepareUri(row['parque']))

        status_uris = {}
        # for age_status in statuses:
        #     status_uris[age_status] = URIRef(prepareUri(age_status))
        print(status_uris)
        collection_uri = URIRef(prepareUri(f"collection-of-trees-LocatedIn-{row['parque']}"))
        stats_uri = URIRef(prepareUri(f"measures-{file_date}-{row['parque']}"))

        
        g.add((park_uri, RDF.type, sio.site))
        g.add((park_uri, RDFS.label, Literal(str(row['parque']).lower())))
        g.add((collection_uri, RDF.type, sio.Collection))
        print(statuses)
        for age_status in statuses:
            # age_status_uri = URIRef(prepareUri(age_status))
            age_status_uri = URIRef(str(collection_uri) + '-life-Status-' + age_status.lower())
            print(age_status_uri)
            g.add((age_status_uri, RDF.type, sio.LifeStatus))
            #g.add((sio.LifeStatus, RDF.type, ppo.LifeStatus))
            g.add((age_status_uri, sio.hasQuality, Literal(age_status)))
            g.add((age_status_uri, RDF.type, sio.MemberCount))
            g.add((age_status_uri, sio.hasValue, Literal(row[age_status], datatype=XSD.integer)))
            g.add((age_status_uri, sio.hasUnit, obo.UO_0000189))
            g.add((age_status_uri, sio.measuredAt, Literal(file_date, datatype=XSD.date)))


        for statistics in stats_col:
            #print('toto')
            # age_status_uri = URIRef(prepareUri(age_status))
            statistics_uri = URIRef(str(stats_uri) + '-SpatialQuantity-' + statistics.lower())
            print(statistics_uri)
            g.add((statistics_uri, RDF.type, sio.DimensionalQuantity))
            g.add((statistics_uri, sio.hasQuality, Literal(age_status)))
            g.add((statistics_uri, sio.hasValue, Literal(row[age_status], datatype=XSD.float)))
            if stats_col == 'altura_promedio_(m)':
                g.add((statistics_uri, sio.hasUnit, obo.UO_0000008)) #mts
            else:
                g.add((statistics_uri, sio.hasUnit, obo.UO_0000007)) #cmts
            g.add((statistics_uri, sio.measuredAt, Literal(file_date, datatype=XSD.date)))
        

        # g.add((status_uri, RDF.type, sio.LifeStatus))
        # g.add((status_uri, RDFS.label, Literal(str(row[age_status]).lower())))



# print(g.serialize(format='turtle'))
#g.serialize('outputs/rdflib-output3.ttl', format='turtle')
outputfile = 'outputs/rdflib-output3.ttl'
g.serialize(outputfile, format='turtle')
print(f'finished....' + outputfile)


# # ## Example with columns header
# # # :PARQUE rdf:type sio:Site .
# # # :PARQUE sio:contains :collection-of-ESPECIE-STATUS .
# # # :collection-of-ESPECIE-STATUS rdf:type sio:Collection .
# # # :collection-of-trees sio:hasAttribute :age .
# # # :age a :subClassOf sio:dimensional-quantity .
# # # :age sio: has-label :lifeCycleInfo .
# # # :lifeCycleInfo sio:has-label "Recien plantado y no consolidado" .
# # # :Recien plantado y no consolidado a sio:memberCount .
# # # :membercount sio:has-value "Recien plantado y no consolidado" .
# # # :lifeCycleInfo sio:has-label "Recien plantado y no consolidado" .
# # # :Recien plantado y no consolidado a sio:memberCount .
# # # :membercount sio:has-value "Recien plantado y no consolidado" .
# # # :lifeCycleInfo sio:has-label "Joven" .
# # # :Joven a sio:memberCount .
# # # :membercount sio:has-value "Joven" .  
# # # :collection-of-trees sio:hasAttribute : Maduro .
# # # :Maduro a sio:mean .
# # # :Maduro sio: has-value "Maduro" .
# # # :collection-of-trees sio:hasAttribute : Viejo .
# # # :Viejo a sio:mean .
# # # :Viejo sio: has-value "Viejo" .

# # ## Example with values
# # # Estado_arbolado_ParquesHistoricoSingularesForestales_YYYY.csv
# # ######## Turtle syntax ########

# # # :Parque-Madrid-Rio rdf:type :Park .
# # # Park sio: isLocatedIn District .
# # # :Parques-Madrid-Rio sio:contains :collection-of-trees .
# # # :collection-of-trees a sio:Collection .
# # # :collection-of-trees sio:hasAttribute :age .
# # # :age a :subClassOf sio:dimensional-quantity .
# # # :age sio: has-label :lifeCycleInfo .
# # # :lifeCycleInfo sio:has-value "New" .
# # # :lifeCycleInfo a sio:memberCount .
# # # :cph_count sio:has-value "8" .  
# # # :collection-of-trees sio:hasAttribute : averageHeight-Parque-Madrid-Rio .
# # # :averageHeight a sio:mean .
# # # :averageHeight-Parque-Madrid-Rio sio: has-value "5.99" .
# # # :collection-of-trees sio:hasAttribute :circumference-Parque-Madrid-Rio .
# # # :circumference-Parque-Madrid-Rio a sio:dimensional-quantity .
# # # :circumference-Parque-Madrid-Rio sio: has-value "32.49" .




# print(g.serialize(format='turtle'))
# g.serialize('outputs/rdflib-output3.ttl', format='turtle')