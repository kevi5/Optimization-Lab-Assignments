import gurobipy as gp
from gurobipy import GRB

x=["1","2","3","4","5"]
model=gp.Model()
x=model.addVars(x,name="x")
model.addConstr(11*x["1"]+53*x["2"]+5*x["3"]+5*x["4"]+29*x["5"]<=40,"c1")
model.addConstr(3*x["1"]+6*x["2"]+5*x["3"]+x["4"]+34*x["5"]<=20,"c1")
for i in x:
    model.addConstr(x[i]>=0,"c2[{i}]")
    model.addConstr(x[i]<=1,"c3[{i}]")
obj=13*x["1"]+16*x["2"]+16*x["3"]+14*x["4"]+39*x["5"]
model.setObjective(obj, GRB.MAXIMIZE)
model.optimize()
for v in model.getVars():
    print(v.varName,v.x)
print("max : ",obj.getValue())