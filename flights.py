__author__ = 'Rayna Todorcheva'

#     Released under the GNU General Public License
#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
#
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <http://www.gnu.org/licenses/>.

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
#         print '-------------------'


# t_max is the maximum wait time at the booth queue
t_max = int(raw_input('Enter a maximum waiting time at the queue (in minutes): '))

# T = one day. "t" is the interval of time on which T is divided
t = int(raw_input('Enter time intervals (in minutes): '))

# b_k is the booth processing time - how much time for 1 passanger
b_k = int(raw_input('Enter booth processing time (in minutes): '))
y_k = 1.0/b_k

# Arrival rate of the passenger at the queue - number of passengers per unit of time (10 minutes)
# a_rate = np.random.poisson(20, 1)
a_rate = int(raw_input('Enter Arrival rate (number of passengers per minute): '))


print 'The max wait time at the queues is set to ', t_max, ' minutes'
print 'Time intervals are set to ', t, ' minutes'
print 'The booth processing time is ', b_k, ' minutes'
print 'The arrival rate is : ', a_rate
print 'Processing rate is : ', y_k

# determine number of booths needed for a set interval of time
num_booths = a_rate/y_k
print 'Number of booths needed is: ', num_booths
