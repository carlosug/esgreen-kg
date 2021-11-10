import csv
import unicodedata
import os
import glob
import pandas as pd
# adapted from here: https://gist.github.com/Gabriel-Chen/774801e1fc7a28265f57e5c3642b25dc
# solutions here: https://coderedirect.com/questions/409995/remove-special-characters-from-csv-file-using-python
# def strip_accents(text):
#     try:
#         text = unicode(text, 'utf-8')
#     except NameError:
#         pass
#     text = unicodedata.normalize('NFD', text).encode('ascii', 'ignore').decode("utf-8")
#     return str(text)


# def remove_accent (feed):
#     csv_f = open(feed, encoding='latin-1', mode='r')
#     csv_str = csv_f.read()
#     csv_str_removed_accent = unicodedata.normalize('NFD', csv_str).encode('ascii', 'ignore').decode("utf-8")
#     csv_f.close()
#     csv_f = open(feed, 'w')
#     csv_f.write(csv_str_removed_accent)
#     return True


# weak solution

# with open('data/inputs/preprocessing/ArboladoZonasVerdesDistritosCalles_2020.csv', 'r') as infile, open("other.csv", 'w') as outfile:
#     read = csv.reader(infile)
#     writer = csv.writer(outfile)
#     for row in read:
#         for element in row:
#             newrow = strip_accents(element)
#             writer.writerow(newrow)



# # path to the files
# esgreendir = 'data/inputs/preprocessing/'

# # get all the csv files
# csvfiles = glob.glob(os.path.join(esgreendir, '*.csv'))

# # loop through files and read them in with pandas
# dataframes = []
# for csvfile in csvfiles:
#     df = pd.read_csv(csvfile)
#     dataframes.append(df)
#     pattern = r"^;Total:;(.*?)$"
#     result = pd.Series(pattern).str.replace('f.', 'ba', regex=True)

# # print out to a new csv file
# result.to_csv('all.csv')

# import unicodedata
# import csv

# def remove_accent (feed):
#     csv_f = open(feed, encoding='latin-1', mode='r')
#     csv_str = csv_f.read()
#     csv_str_removed_accent = unicodedata.normalize('NFD', csv_str).encode('ascii', 'ignore').decode("utf-8")
#     csv_f.close()
#     csv_f = open(feed, 'w')
#     csv_f.write(csv_str_removed_accent)
#     return True

# if __name__ == "__main__":
#     remove_accent('data/inputs/preprocessing/ArboladoParquesHistoricoSingularesForestales_2019.csv')



def preprocessing (feed):
    csv_f = open(feed, encoding='latin-1', mode='r')
    csv_str = csv_f.read()
    csv_str_removed_all = unicodedata.normalize('NFD', csv_str).encode('ascii', 'ignore').decode("utf-8").replace(' ', '_').lower()
    csv_f.close()
    csv_f = open(feed, 'w')
    csv_f.write(csv_str_removed_all)
    return True

# if __name__ == "__main__":
#     remove_accent('data/inputs/preprocessing/MasasZonasVerdesDistritosCalles_2019.csv')


    # path to the files
esgreendir = 'data/inputs/preprocessing/'

# get all the csv files
csvfiles = glob.glob(os.path.join(esgreendir, '*.csv'))

# loop through files and read them in with pandas
for csvfile in csvfiles:
    preprocessing(csvfile)