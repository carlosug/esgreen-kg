# FOR EACH DATASET RETRIEVE UNIQUE ESPECIE

import requests
import pandas as pd #for handling csv and csv contents
import unicodedata
import re
import fileinput
import csv
import glob
import os


    # path to the files
esgreeninputs = 'data/inputs/'

# get all the csv files
csvfiles = glob.glob(os.path.join(esgreeninputs, '*.csv'))

for csvfile in csvfiles:
    # Read in the csv file
    csv_f = open(csvfile, encoding='latin-1', mode='r')
    csv_str = csv_f.read()
    df = pd.read_csv(csvfile)
    print(df)

    # for col in csvfile:
    #     especie_col = 'especie'        
    #     list_especies = df[especie_col]
    #     unique_especies = []
    #     for especie in list_especies:
    #         if especie not in unique_especies:
    #           unique_especies.append(especie)
    #         print(especie)

# #specie = 'aesculus_hippocastanum'

#     for specie in unique_especies:
#         res = requests.get(f'https://www.wikidata.org/w/api.php?action=wbsearchentities&search={specie}&language=en&format=json')
#         print(specie,res.json())



#     list_parks = df[park_col]
#     unique_parks = []
#     for park in unique_parks:
#         if especie not in unique_especies:
#             unique_especies.append(especie)

# #specie = 'aesculus_hippocastanum'

#     for specie in unique_especies:
#         res = requests.get(f'https://www.wikidata.org/w/api.php?action=wbsearchentities&search={specie}&language=en&format=json')
#         print(specie,res.json())
# # import pandas as pd

# # # tsv_file = open('data/inputs/data_eol.tsv')
# # # read_tsv = csv.reader(tsv_file, delimiter='\t')

# # # for row in read_tsv:
# # #     print(row)



# # eol_data = pd.read_csv('data/inputs/data_eol.tsv', sep = '\t',low_memory=False)
# # print(eol_data.head())

# # print(eol_data.columns)
# # scientific_name = 'Scientific Name'
# # print(eol_data[scientific_name] == 'pinus')
# # target = 'Target EOL ID'
# # # for index, row in eol_data.iterrows():
# # #         print(row[target] for scientific_name == "pinus")