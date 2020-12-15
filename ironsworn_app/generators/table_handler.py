import os
import csv


def random_table_handler(table_name, result):

    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'datas/{}.csv'.format(table_name))

    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')

        for row in reader:
            if row[0] == str(result):
                return row[1]


