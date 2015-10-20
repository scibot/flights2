__author__ = 'Rayna Todorcheva'

import csv
import time
import numpy as np

# with open('flights_data.csv', 'rb') as f:
#     mycsv = csv.reader(f)
#     for row in mycsv:
#         flight_time = row[0]
#         num_passengers = row[1]
#         flight_number = row[2]
#         print 'Flight Number: ', flight_number
#         print 'Arrives at: ', time.strftime("%H:%M:%S", time.gmtime(float(flight_time)*60))
#         print 'With ',num_passengers ,'passengers.'
#         print '--------------'


# t_max is the maximum wait time at the booth queue
t_max = int(raw_input('Enter a maximum waiting time at the queue (in minutes): '))

# T = one day. "t" is the interval of time on which T is divided
t = int(raw_input('Enter time intervals (in minutes): '))

# b_t is the booth processing time
b_t = int(raw_input('Enter booth processing time (in minutes): '))

# Arrival rate of the passenger at the queue - number of passengers per unit of time (10 minutes)
a_rate = np.random.poisson(20, 100)

print 'The max wait time at the queues is set to ', t_max, ' minutes'
print 'Time intervals are set to ', t, ' minutes'
print 'The booth processing time is ', b_t, ' minutes'
print 'The arival rate is : ', a_rate

