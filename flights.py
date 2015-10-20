__author__ = 'Rayna Todorcheva'

import csv
import sys


f = open('flights_data.csv', 'rb' )
try:
    reader = csv.reader(f, delimiter=',')
    my_data_list = []
    for row in reader:
        print row[0:2]
        my_data_list.append(row)
finally:
    f.close()