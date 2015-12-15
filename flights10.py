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

#lenght (in minutes) which will divide time period in the output file in `time_step`-number of rows
#time interval in minutes used for defining time periods, and also affects arrival rate and booth_processing time
time_step = int(raw_input('Enter time_step (time interval in minutes): '))

#c constant
c = int(raw_input('Enter constant c (# integer, c > 1 ): '))

#alpha constant
alpha = float(raw_input('Enter constant alpha (# float, 0 < alpha < 1 ): '))

# results from 0:00 to 0:00 + time_period
time_period = int(raw_input('Enter time period (in minutes): '))

#booth change schedule
booth_change = int(raw_input('Enter booth change time (in minutes, bigger than the time_step): '))

#print time_period/time_step
#print time_period/booth_change+1

while (time_period/time_step < time_period/booth_change+1):
    booth_change = int(raw_input('Please enter bigger booth change time (in minutes, bigger than time_step): '))

# t_max is the maximum wait time at the booth queue
t_max = int(raw_input('Enter a maximum waiting time at the queue (in minutes): '))
t_total = time_period + t_max
#print 'The total time is:', t_total

# Booth processing time
b_rate = int(raw_input('Enter booth processing rate (# passengers per ' + str(time_step) + ' minutes): '))
y_k = float(b_rate)/time_step

arrival_rates = []
arr_rates_by_minute = []


with open('flights_dataThree.csv', 'rb') as f:
    mycsv = csv.reader(f)
    out_file1 = open("output1.csv", 'wb')
    writer1 = csv.writer(out_file1)
    out_file3 = open("output3.csv", 'wb')
    writer3 = csv.writer(out_file3)
    for row in mycsv:
        flight_time = row[0]
        num_passengers = row[1]
        flight_number = row[2]
        flight_time = int(flight_time)
        num_passengers = int(num_passengers)

        #round up flight times in minutes
        #begin output3.csv
        travel_min = pow(num_passengers, alpha)
        travel_max = c * pow(num_passengers, alpha)

        #first passenger of a flight out
        flight_in = math.ceil(flight_time + travel_min)
        

        #flight end time
        flight_out = math.ceil(flight_time + travel_max)
        ar_rate = num_passengers / (travel_max - travel_min)
        writer3.writerow([flight_number, flight_in, flight_out, ar_rate])
        #end output3.csv

        # add_to(a_rate)
        # print 'Flight Number: ', flight_number
        # print 'Arrives at: ', time.strftime("%H:%M:%S", time.gmtime(float(flight_time) * 60))
        # print 'With ', num_passengers, 'passengers'
        # print 'start_time is', flight_time
        # # t is total passengers arriving time from a flight
        # print 'end_time is: ', flight_out
        # row.append(flight_out)
        # writer1.writerow(row)
        # # flight arrival interval
        # time_from = time.strftime("%H:%M:%S", time.gmtime(float(flight_time) * 60))
        # time_to = time.strftime("%H:%M:%S", time.gmtime(float(flight_out) * 60))
        # print 'time from:', time_from
        # print 'time to:', time_to
        # print '-------------------'


    out_file1.close()
    out_file3.close()
    # write second output2 file


# Create the 'prob' variable to contain the problem data
prob = LpProblem("The Booth Minimizing Problem", LpMinimize)

#x = 1 : N
x = []

#0:00 - time_period - divided by booth_change
for i in xrange(0, t_total, booth_change):
    x.append(LpVariable("B" + str(i/booth_change), 0, 500, LpInteger))

N = time_period/booth_change

#sum 1 .. N
# The objective function is added to 'prob' first
prob += lpSum(x[i] for i in range(N+1)), "# of Booth Hours"

#calculate arr_rate by minute for subperiod defined by time_step
def period_arr_rate_by_minutes(time_from):

    #period_arr_rate contains arr_rates from 0 to 9th minute
    #if periods should override, i.e. 1st - 0 -> 10th, 2nd - 10 -> 20th minute,
    #just add 1 to time_to

    time_to = time_from + time_step
    period_arr_rate = 0
    # print "\n"
    # print "checking from", time_from, "to", time_to
    # print "\n"

    #for loop period by minute
    for minute in range(time_from, time_to):
        rate_in_minute = 0
        #for loop flights from csv
        for row in arr_rates_data:
            flight_start = int(float(row[1]))
            flight_end = int(float(row[2]))
            #check flight interval for containing current minute
            if (flight_start <= minute < flight_end):
                # print "minute", minute , "exists in interval", flight_start , "-", flight_end,  "flight", row[0]
                rate_in_minute += float(row[3])

        #print "minute:", minute, "arr_rate:" , rate_in_minute
        arr_rates_by_minute.insert(minute, rate_in_minute)
        #add minute arr_rate to period arr rate and save for later usage
        period_arr_rate += rate_in_minute



    arrival_rates.append(period_arr_rate)
    #print "arrival_rates", arrival_rates

    return period_arr_rate

#for period (0, time_to), get arr_rate for subperiods defined by time_step from arrival_rates list
# or calculate it and save for later
def get_period_arr_rate(time_to):
    result = 0;

    for time in xrange(0, time_to, time_step):
        i =  time/time_step;
        if (len(arrival_rates) > i):
            result += arrival_rates[i]
        else:
            result += period_arr_rate_by_minutes(time)

    return result


# The constraints are entered
print x

#list from 0 to t_total with step time_step
times = [time_step * i for i in range(0,(time_period)/time_step)]

#print times

with open('output3.csv', 'rb') as f:
    arr_rates_csv = csv.reader(f)
    arr_rates_data = list(arr_rates_csv)

for j in range(0, len(times)):
    period_arr_rate = get_period_arr_rate(times[j] + t_max)
    #print "period", times[j], "arr_rate", period_arr_rate

    if (times[j]+t_max <= booth_change):
        prob += y_k * x[0] * (times[j] + t_max) >= period_arr_rate
    else:
        m = (times[j]+t_max) / booth_change
        r = (times[j]+t_max) - m * booth_change
        #print "time ", times[j]
        #print m
        #print r
        prob += lpSum([booth_change*y_k * x[i] for i in range(0,m)]) + y_k*x[m] * r >= period_arr_rate

#print "arr_rates_by_minute", len(arr_rates_by_minute)


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

