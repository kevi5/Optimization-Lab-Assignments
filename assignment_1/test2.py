from gurobipy import *

m = Model()
x = m.addVar(lb =0, name='x')
y = m.addVar(lb= 0, name='y')
m.addConstr(x-y==1)
m.setObjective(x**2 + y**2, GRB.MINIMIZE)
m.optimize()
print('Optimal x = ' + str(x.x))
print('Optimal x = ' + str(y.x))
print('Optimal objective = ' + str(m.ObjVal))