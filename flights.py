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
from pulp import *


# Arrival rate of the passenger at the queue - number of passengers per unit of time (10 minutes)
# a_rate = np.random.poisson(20, 1)
#a_rate = int(raw_input('Enter Arrival rate (number of passengers per minute): '))
a_rate = [0,0,0,0,0,0,0,0,0,0,0,0,
          0,0,0,0,0,0,0,0,0,0,0,0]


def addto (a_rate):
    if flight_time in range(0,60):
        a_rate[0] += int(num_passengers)
    elif flight_time in range(60,120):
        a_rate[1] += int(num_passengers)
    elif flight_time in range(120,180):
        a_rate[2] += int(num_passengers)
    elif flight_time in range(180,240):
        a_rate[3] += int(num_passengers)
    elif flight_time in range(240,300):
        a_rate[4] += int(num_passengers)
    elif flight_time in range(300,360):
        a_rate[5] += int(num_passengers)
    elif flight_time in range(360,420):
        a_rate[6] += int(num_passengers)
    elif flight_time in range(420,480):
        a_rate[7] += int(num_passengers)
    elif flight_time in range(480,540):
        a_rate[8] += int(num_passengers)
    elif flight_time in range(540,600):
        a_rate[9] += int(num_passengers)
    elif flight_time in range(600,660):
        a_rate[10] += int(num_passengers)
    elif flight_time in range(660,720):
        a_rate[11] += int(num_passengers)
    elif flight_time in range(720,780):
        a_rate[12] += int(num_passengers)
    elif flight_time in range(780,840):
        a_rate[13] += int(num_passengers)
    elif flight_time in range(840,900):
        a_rate[14] += int(num_passengers)
    elif flight_time in range(900,960):
        a_rate[15] += int(num_passengers)
    elif flight_time in range(960,1020):
        a_rate[16] += int(num_passengers)
    elif flight_time in range(1020,1080):
        a_rate[17] += int(num_passengers)
    elif flight_time in range(1080,1140):
        a_rate[18] += int(num_passengers)
    elif flight_time in range(1140,1200):
        a_rate[19] += int(num_passengers)
    elif flight_time in range(1200,1260):
        a_rate[20] += int(num_passengers)
    elif flight_time in range(1260,1320):
        a_rate[21] += int(num_passengers)
    elif flight_time in range(1320,1380):
        a_rate[22] += int(num_passengers)
    elif flight_time in range(1380,1440):
        a_rate[23] += int(num_passengers)
    else:
        print "outside the allowed range"
    return

with open('flights_data.csv', 'rb') as f:
    mycsv = csv.reader(f)
    for row in mycsv:
        flight_time = row[0]
        num_passengers = row[1]
        flight_number = row[2]
        flight_time = int(flight_time)
        addto(a_rate)
        print 'Flight Number: ', flight_number
        print 'Arrives at: ', time.strftime("%H:%M:%S", time.gmtime(float(flight_time)*60))
        print 'With ',num_passengers ,'passengers'
        print '-------------------'

print a_rate
# t_max is the maximum wait time at the booth queue
# t_max = int(raw_input('Enter a maximum waiting time at the queue (in minutes): '))

# T = one day. "t" is the interval of time on which T is divided
#t = int(raw_input('Enter time intervals (in minutes): '))
# t = 1 # hour

# b_k is the booth processing time - how much time for 1 passanger
y_k = int(raw_input('Enter booth processing rate (# passengers per hour): '))
#y_k = 1.0/b_k


# Create the 'prob' variable to contain the problem data
prob = LpProblem("The Booth Minimize Problem",LpMinimize)

# The 2 variables Booth are created with a lower limit of zero
x1=LpVariable("From 12:00 am to 1:00 am",0,None,LpInteger)
x2=LpVariable("From 1:00 am to 2:00 am",0,None,LpInteger)
x3=LpVariable("From 2:00 am to 3:00 am",0,None,LpInteger)
x4=LpVariable("From 3:00 am to 4:00 am",0,None,LpInteger)
x5=LpVariable("From 4:00 am to 5:00 am",0,None,LpInteger)
x6=LpVariable("From 5:00 am to 6:00 am",0,None,LpInteger)
x7=LpVariable("From 6:00 am to 7:00 am",0,None,LpInteger)
x8=LpVariable("From 7:00 am to 8:00 am",0,None,LpInteger)
x9=LpVariable("From 8:00 am to 9:00 am",0,None,LpInteger)
x10=LpVariable("From 9:00 am to 10:00 am",0,None,LpInteger)
x11=LpVariable("From 10:00 am to 11:00 am",0,None,LpInteger)
x12=LpVariable("From 11:00 am to 12:00 pm",0,None,LpInteger)
x13=LpVariable("From 12:00 pm to 1:00 pm",0,None,LpInteger)
x14=LpVariable("From 1:00 pm to 2:00 pm",0,None,LpInteger)
x15=LpVariable("From 2:00 pm to 3:00 pm",0,None,LpInteger)
x16=LpVariable("From 3:00 pm to 4:00 pm",0,None,LpInteger)
x17=LpVariable("From 4:00 pm to 5:00 pm",0,None,LpInteger)
x18=LpVariable("From 5:00 pm to 6:00 pm",0,None,LpInteger)
x19=LpVariable("From 6:00 pm to 7:00 pm",0,None,LpInteger)
x20=LpVariable("From 7:00 pm to 8:00 pm",0,None,LpInteger)
x21=LpVariable("From 8:00 pm to 9:00 pm",0,None,LpInteger)
x22=LpVariable("From 9:00 pm to 10:00 pm",0,None,LpInteger)
x23=LpVariable("From 10:00 pm to 11:00 pm",0,None,LpInteger)
x24=LpVariable("From 11:00 pm to 12:00 am",0,None,LpInteger)


# The objective function is added to 'prob' first
prob += x1 + x2 + x3, "# of Booth Hours"

# The five constraints are entered
prob += y_k*x1 >= a_rate[0], "From 12:00 am to 1:00 am"
prob += y_k*x2 >= a_rate[1], "Form 1:00 am to 2:00 am"
prob += y_k*x3 >= a_rate[2], "From 2:00 am to 3:00 am"
prob += y_k*x4 >= a_rate[3], "From 3:00 am to 4:00 am"
prob += y_k*x5 >= a_rate[4], "From 4:00 am to 5:00 am"
prob += y_k*x6 >= a_rate[5], "From 5:00 am to 6:00 am"
prob += y_k*x7 >= a_rate[6], "From 6:00 am to 7:00 am"
prob += y_k*x8 >= a_rate[7], "From 7:00 am to 8:00 am"
prob += y_k*x9 >= a_rate[8], "From 8:00 am to 9:00 am"
prob += y_k*x10 >= a_rate[9], "From 9:00 am to 10:00 am"
prob += y_k*x11 >= a_rate[10], "From 10:00 am to 11:00 am"
prob += y_k*x12 >= a_rate[11], "From 11:00 am to 12:00 am"
prob += y_k*x13 >= a_rate[12], "From 12:00 am to 1:00 pm"
prob += y_k*x14 >= a_rate[13], "From 1:00 pm to 2:00 pm"
prob += y_k*x15 >= a_rate[14], "From 2:00 pm to 3:00 pm"
prob += y_k*x16 >= a_rate[15], "From 3:00 pm to 4:00 pm"
prob += y_k*x17 >= a_rate[16], "From 4:00 pm to 5:00 pm"
prob += y_k*x18 >= a_rate[17], "From 5:00 pm to 6:00 pm"
prob += y_k*x19 >= a_rate[18], "From 6:00 pm to 7:00 pm"
prob += y_k*x20 >= a_rate[19], "From 7:00 pm to 8:00 pm"
prob += y_k*x21 >= a_rate[20], "From 8:00 pm to 9:00 pm"
prob += y_k*x22 >= a_rate[21], "From 9:00 pm to 10:00 pm"
prob += y_k*x23 >= a_rate[22], "From 10:00 pm to 11:00 pm"
prob += y_k*x24 >= a_rate[23], "From 10:00 pm to 12:00 am"



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

