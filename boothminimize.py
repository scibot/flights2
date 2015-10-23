__author__ = 'Rayna Todorcheva'

# Import PuLP modeler functions
from pulp import *

# Create the 'prob' variable to contain the problem data
prob = LpProblem("The Booth Minimize Problem",LpMinimize)

# The 2 variables  Booth1 and Booth2 are created with a lower limit of zero
x1=LpVariable("Booth in period 1",0,None,LpInteger)
x2=LpVariable("Booth in period 2",0,None,LpInteger)
x3=LpVariable("Booth in period 3",0,None,LpInteger)

# The objective function is added to 'prob' first
prob += x1 + x2 + x3, "# of Booth Hours"

# The five constraints are entered
prob += 100*x1 >= 300, "First period"
prob += 100*x2 >= 500, "Second period"
prob += 100*x3 >= 150, "Third period"


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
