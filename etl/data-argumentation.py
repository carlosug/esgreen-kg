import requests
import pandas as pd #for handling csv and csv contents
import unicodedata
import re
import fileinput
import csv

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
        park_col = 'parque'
        #print(f'if',count_col, especie_col, file_date)
    else:
        file_date = file_date.replace('_', '')
        count_col = 'unidades_' + file_date
        especie_col = 'especie'
        park_col = 'parque'
        
    list_especies = df[especie_col]
    unique_especies = []
    for especie in list_especies:
        if especie not in unique_especies:
            unique_especies.append(especie)

#specie = 'aesculus_hippocastanum'
# for gbif: https://data-blog.gbif.org/post/downloading-long-species-lists-on-gbif/
    for specie in unique_especies:
        res = requests.get(f'https://www.wikidata.org/w/api.php?action=wbsearchentities&search={specie}&language=en&format=json')
        print(specie,res.json())



    list_parks = df[park_col]
    unique_parks = []
    for park in unique_parks:
        if especie not in unique_especies:
            unique_especies.append(especie)

#specie = 'aesculus_hippocastanum'

    for specie in unique_especies:
        res = requests.get(f'https://www.wikidata.org/w/api.php?action=wbsearchentities&search={specie}&language=en&format=json')
        print(specie,res.json())
# import pandas as pd

# # tsv_file = open('data/inputs/data_eol.tsv')
# # read_tsv = csv.reader(tsv_file, delimiter='\t')

# # for row in read_tsv:
# #     print(row)



# eol_data = pd.read_csv('data/inputs/data_eol.tsv', sep = '\t',low_memory=False)
# print(eol_data.head())

# print(eol_data.columns)
# scientific_name = 'Scientific Name'
# print(eol_data[scientific_name] == 'pinus')
# target = 'Target EOL ID'
# # for index, row in eol_data.iterrows():
# #         print(row[target] for scientific_name == "pinus")