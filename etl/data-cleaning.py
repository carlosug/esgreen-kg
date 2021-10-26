import unidecode
import csv
import re
import fileinput

def remove_accent (feed):
    csv_f = open(feed, encoding='latin-1', mode='r')
    csv_str = csv_f.read()
    csv_str_removed_accent = unidecode.unidecode(csv_str)
    csv_f.close()
    csv_f = open(feed, 'w')
    csv_f.write(csv_str_removed_accent)
    return True

if __name__ == "__main__":
    remove_accent('data/inputs/ArboladoParquesHistoricoSingularesForestales_2019.csv')


pattern = r"^;Total:;(.*?)$"

for line in fileinput.input(r'data/inputs/ArboladoParquesHistoricoSingularesForestales_2019.csv', inplace = True):
   if not re.search(pattern, line):
      print(line, end="")