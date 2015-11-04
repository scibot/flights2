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
import time
import numpy as np
from datetime import datetime
from pulp import *


# Arrival rate of the passenger at the queue - number of passengers per unit of time (10 minutes)

ar_rate = int(raw_input('Enter arrival rate (# passengers per 1 minutes): '))
# results from 0:00 to 0:00 + time_period
time_period = int(raw_input('Enter time period(in minutes): '))

# t_max is the maximum wait time at the booth queue
t_max = int(raw_input('Enter a maximum waiting time at the queue (in minutes): '))
t_total = time_period + t_max
print 'The total time is:', t_total

# Booth processing time
y_k = int(raw_input('Enter booth processing rate (# passengers per 10 minutes): '))
# y_k = 1.0/b_k


# create time periods
output2_rows = []
for i in xrange(0, time_period + 10, 10):
    time_is = time.strftime("%H:%M:%S", time.gmtime(float(i) * 60))
    output2_rows.append([time_is, 0])

with open('flights_data2.csv', 'rb') as f:
    mycsv = csv.reader(f)
    out_file1 = open("output1.csv", 'wb')
    writer1 = csv.writer(out_file1)
    out_file2 = open("output2.csv", 'wb')
    writer2 = csv.writer(out_file2)
    for row in mycsv:
        timetable = []
        flight_time = row[0]
        num_passengers = row[1]
        flight_number = row[2]
        flight_time = int(flight_time)
        num_passengers = int(num_passengers)
        # add_to(a_rate)
        print 'Flight Number: ', flight_number
        print 'Arrives at: ', time.strftime("%H:%M:%S", time.gmtime(float(flight_time) * 60))
        print 'With ', num_passengers, 'passengers'
        print 'start_time is', flight_time
        # t is total passenger traveling time from the gate to boot line
        t = num_passengers / ar_rate
        print 'The total passenger travel time is:', t
        total_time = flight_time + t
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
        for idx, output2_row in enumerate(output2_rows):
            if (time_from <= output2_row[0] and output2_row[0] <= time_to ):
                output2_rows[idx][1] += 1
                #print "Flight in period: ", output2_rows[idx][0]

    out_file1.close()
    # write second output2 file
    for output2_row in output2_rows:
        writer2.writerow(output2_row)

    out_file2.close()

total_arrival_rate = 0
with open('output2.csv', 'rb') as f:
    times_csv = csv.reader(f)
    for row in times_csv:
        # difference in minutes between 0:00:00 and current time
        start = datetime.strptime("0:00:00", "%H:%M:%S")
        end = datetime.strptime(row[0], "%H:%M:%S")
        diff = end - start
        minutes = (diff.days * 1440) + (diff.seconds / 60)
        print "Elapsed minutes: ", minutes
        # time_in_minutes * planes_in_that_time * arrival_rate
        total_arrival_rate += minutes * int(row[1]) * ar_rate

print "Total arrival rate: ", total_arrival_rate

# Create the 'prob' variable to contain the problem data
prob = LpProblem("The Booth Minimize Problem", LpMinimize)

# The 2 variables  Booth1 and Booth2 are created with a lower limit of zero
# x1 = LpVariable("From 12:00 am to 1:00 am", 0, None, LpInteger)
# x2 = LpVariable("From 1:00 am to 2:00 am", 0, None, LpInteger)
# x3 = LpVariable("From 2:00 am to 3:00 am", 0, None, LpInteger)
# x4 = LpVariable("From 3:00 am to 4:00 am", 0, None, LpInteger)
# x5 = LpVariable("From 4:00 am to 5:00 am", 0, None, LpInteger)
# x6 = LpVariable("From 5:00 am to 6:00 am", 0, None, LpInteger)
# x7 = LpVariable("From 6:00 am to 7:00 am", 0, None, LpInteger)
# x8 = LpVariable("From 7:00 am to 8:00 am", 0, None, LpInteger)
# x9 = LpVariable("From 8:00 am to 9:00 am", 0, None, LpInteger)
# x10 = LpVariable("From 9:00 am to 10:00 am", 0, None, LpInteger)
# x11 = LpVariable("From 10:00 am to 11:00 am", 0, None, LpInteger)
# x12 = LpVariable("From 11:00 am to 12:00 pm", 0, None, LpInteger)
# x13 = LpVariable("From 12:00 pm to 1:00 pm", 0, None, LpInteger)
# x14 = LpVariable("From 1:00 pm to 2:00 pm", 0, None, LpInteger)
# x15 = LpVariable("From 2:00 pm to 3:00 pm", 0, None, LpInteger)
# x16 = LpVariable("From 3:00 pm to 4:00 pm", 0, None, LpInteger)
# x17 = LpVariable("From 4:00 pm to 5:00 pm", 0, None, LpInteger)
# x18 = LpVariable("From 5:00 pm to 6:00 pm", 0, None, LpInteger)
# x19 = LpVariable("From 6:00 pm to 7:00 pm", 0, None, LpInteger)
# x20 = LpVariable("From 7:00 pm to 8:00 pm", 0, None, LpInteger)
# x21 = LpVariable("From 8:00 pm to 9:00 pm", 0, None, LpInteger)
# x22 = LpVariable("From 9:00 pm to 10:00 pm", 0, None, LpInteger)
# x23 = LpVariable("From 10:00 pm to 11:00 pm", 0, None, LpInteger)
# x24 = LpVariable("From 11:00 pm to 12:00 am", 0, None, LpInteger)


booth_change = 10
N = time_period/booth_change
x = pulp.LpVariable("From", 0, None, LpInteger)

# The objective function is added to 'prob' first
prob += sum(x[i] for i in N), "# of Booth Hours"

upperL = t_total/booth_change
remainder = t_total - upperL * booth_change


# The constraints are entered
prob += sum([y_k * x[i] for i in upperL]) + y_k * x[upperL + 1] * remainder >= total_arrival_rate


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
#print "Total Booths = ", value(prob.objective)

