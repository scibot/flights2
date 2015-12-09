__author__ = 'Rayna Todorcheva'

# Released under the GNU General Public License
# This program is free software: you can redistribute it and/or modify
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
import math
import time
import numpy as np
import datetime
from pulp import *

#lenght (in minutes) which will divide time period in the output file in `arrival_step`-number of rows
#time interval in minutes used for defining time periods, and also affects arrival rate and booth_processing time
arrival_step = int(raw_input('Enter arrival_step (time interval in minutes): '))

# Arrival rate of the passenger at the queue - number of passengers per unit of time (`arrival_step` minutes)
#ar_rate = int(raw_input('Enter arrival rate (# passengers per ' + str(arrival_step) + ' minutes): '))

#c constant
c = int(raw_input('Enter constant c (# integer, c > 1 ): '))

#alpha constant
alpha = float(raw_input('Enter constant alpha (# float, 0 < alpha < 1 ): '))

# results from 0:00 to 0:00 + time_period
time_period = int(raw_input('Enter time period (in minutes): '))

#booth change schedule
booth_change = int(raw_input('Enter booth change time (in minutes, bigger than the arrival_step): '))

#print time_period/arrival_step
#print time_period/booth_change+1

while (time_period/arrival_step < time_period/booth_change+1):
    booth_change = int(raw_input('Please enter bigger booth change time (in minutes, bigger than arrival_step): '))

# t_max is the maximum wait time at the booth queue
t_max = int(raw_input('Enter a maximum waiting time at the queue (in minutes): '))
t_total = time_period + t_max
print 'The total time is:', t_total

# Booth processing time
y_k = int(raw_input('Enter booth processing rate (# passengers per ' + str(arrival_step) + ' minutes): '))


# create time periods
output2_rows = []
arrival_rates = []
time_begin = time.strftime("%H:%M:%S", time.gmtime(0.0))
output2_rows.append([time_begin, 0])
for i in xrange(0, time_period, arrival_step):
    time_is = time.strftime("%H:%M:%S", time.gmtime(float(i + arrival_step) * 60))
    output2_rows.append([time_is, 0])


with open('flights_dataTest.csv', 'rb') as f:
    mycsv = csv.reader(f)
    out_file1 = open("output1.csv", 'wb')
    writer1 = csv.writer(out_file1)
    out_file2 = open("output2.csv", 'wb')
    writer2 = csv.writer(out_file2)
    out_file3 = open("output3.csv", 'wb')
    writer3 = csv.writer(out_file3)
    for row in mycsv:
        flight_time = row[0]
        num_passengers = row[1]
        flight_number = row[2]
        flight_time = int(flight_time)
        num_passengers = int(num_passengers)

        #begin output3.csv
        #round up travel_min & travel_max in minutes
        travel_min = math.ceil(pow(num_passengers, alpha))

        #flight start time
        flight_time += travel_min
        travel_max = math.ceil(pow(c * num_passengers, alpha))

        #flight end time
        total_time = flight_time + travel_max
        ar_rate = num_passengers / (travel_max - travel_min)
        writer3.writerow([flight_number, flight_time, total_time, ar_rate])
        #end output3.csv

        # add_to(a_rate)
        print 'Flight Number: ', flight_number
        print 'Arrives at: ', time.strftime("%H:%M:%S", time.gmtime(float(flight_time) * 60))
        print 'With ', num_passengers, 'passengers'
        print 'start_time is', flight_time
        # t is total passengers arriving time from a flight
        #t = arrival_step / ar_rate * num_passengers
        #print 'The total passengers arriving time from a flight is:', t
        #total_time = flight_time + t + travel_max
        print 'end_time is: ', total_time
        row.append(total_time)
        writer1.writerow(row)
        # flight arrival interval
        time_from = time.strftime("%H:%M:%S", time.gmtime(float(flight_time) * 60))
        time_to = time.strftime("%H:%M:%S", time.gmtime(float(total_time) * 60))
        print 'time from:', time_from
        print 'time to:', time_to
        print '-------------------'
        # check time periods for current plane
        '''
        for idx, output2_row in enumerate(output2_rows):
            if (idx > 0):
                interval_start = output2_rows[idx-1][0]
                interval_end = output2_rows[idx][0]
                #1 flight ends in this interval => check if time_to is strictly larger than interval_start - :00
                #2 flight starts in this interval => check if time_from is strictly smaller than interval_end - :00
                if ( (time_from <= interval_start < time_to) or (interval_start <= time_from < interval_end) ):
                    output2_rows[idx][1] += 1
                    print "Plane interval " , time_from , " - " , time_to , " overlaps with period " , interval_start , " - " , interval_end
        '''

    out_file1.close()
    out_file3.close()
    # write second output2 file
    '''
    for output2_row in output2_rows:
        writer2.writerow(output2_row)

    out_file2.close()
    '''

total_arrival_rate = 0
'''
with open('output2.csv', 'rb') as f:
    times_csv = csv.reader(f)
    for row in times_csv:
        # difference in minutes between 0:00:00 and current time
        start = datetime.datetime.strptime("0:00:00", "%H:%M:%S")
        end = datetime.datetime.strptime(row[0], "%H:%M:%S")
        diff = end - start
        minutes = (diff.days * 1440) + (diff.seconds / 60)
        #print "Elapsed minutes: ", minutes + arrival_step

        # time_in_minutes * planes_in_that_time * arrival_rate
        total_arrival_rate += minutes * int(row[1]) * ar_rate
'''


print "Total arrival rate: ", total_arrival_rate

# Create the 'prob' variable to contain the problem data
prob = LpProblem("The Booth Minimizing Problem", LpMinimize)

#x1-24 = 1 : N
x = []

#t_total
#0:00 - time_period - divided by booth_change
for i in xrange(0, t_total, booth_change):
    x.append(LpVariable("B" + str(i/booth_change), 0, 50, LpInteger))

N = time_period/booth_change

#sum 1 .. N
# The objective function is added to 'prob' first
prob += lpSum(x[i] for i in range(N)), "# of Booth Hours"

#list from 0 to t_total with step arrival_step
times = [arrival_step * i for i in range(0,time_period/arrival_step)]

def calculate_period_arr_rate(time_from):
    time_to = time_from + arrival_step
    result = 0
    print "checking from", time_from, "to", time_to
    for row in arr_rates_data:
        print "flight time from", row[1], "to", row[2]
        flight_from = int(float(row[1]))
        flight_to = int(float(row[2]))
        if ( (flight_from <= time_from <= flight_to) or (time_from <= flight_from <= time_to) ):
            result += float(row[3])

    arrival_rates.append(result)
    print "arrival_rates", arrival_rates

    return result

def get_period_arr_rate(time_to):
    result = 0;
    for i in range(0, time_to/arrival_step - 1):
        if (len(arrival_rates) > i):
            result += arrival_rates[i]
        else:
            result += calculate_period_arr_rate(i*arrival_step)

    return result


#print times

# The constraints are entered
print x
#times[j] is the time at each arrival step
#j is 0,1,2...times' length
with open('output3.csv', 'rb') as f:
    arr_rates_csv = csv.reader(f)
    arr_rates_data = list(arr_rates_csv)

for j in range(0, len(times)):
    if (times[j]+t_max <= booth_change):
        prob += y_k * x[0] * (times[j] + t_max) >= get_period_arr_rate(times[j] + t_max)
    else:
        m = (times[j]+t_max) / booth_change
        r = (times[j]+t_max) - m * booth_change
        #print "time ", times[j]
        #print m
        #print r
        prob += lpSum([booth_change*y_k * x[i] for i in range(0,m-1)]) + y_k*x[m] * r >= get_period_arr_rate(times[j] + t_max)


# The problem data is written to an .lp file
prob.writeLP("Booths.lp")

# The problem is solved using PuLP's choice of Solver
prob.solve()

# The status of the solution is printed to the screen
print "Status:", LpStatus[prob.status]

# Each of the variables is printed with it's resolved optimum value
for v in prob.variables():
    print v.name, "=", v.varValue

# The optimised objective function value is printed to the screen
print "Total Booths = ", value(prob.objective)

