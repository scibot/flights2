__author__ = 'Rayna Todorcheva'

import csv
import time

with open('flights_data.csv', 'rb') as f:
    mycsv = csv.reader(f)
    for row in mycsv:
        flight_time = row[0]
        num_passengers = row[1]
        flight_number = row[2]
        print 'Flight Number: ', flight_number
        print 'Arrives at: ', time.strftime("%H:%M:%S", time.gmtime(float(flight_time)*60))
        print 'With ',num_passengers ,'passengers.'
        print '--------------'




# f = open('flights_data.csv', 'rb' )
# try:
#     reader = csv.reader(f, delimiter=',')
#     my_data_list = []
#     for row in reader:
#         print row[0:2]
#         my_data_list.append(row)
# finally:
#     f.close()


