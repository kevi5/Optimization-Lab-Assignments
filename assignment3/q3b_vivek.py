import gurobipy as gp
from gurobipy import GRB

J=["1","2","3"]
C=["4","5","6"]
P={("1","4"):2,("2","4"):3,("2","6"):2,("3","4"):1,("3","5"):1}

model = gp.Model()
x = model.addVars(J,C,vtype=GRB.BINARY ,name="x")
for i in J:
    model.addConstr(
        x.sum(i,"*")<=1,name=f"cand[{i}]"
    )
for i in C:
    model.addConstr(
        x.sum("*",i)<=1,name=f"job[{i}]"
    )
# model.addConstr(x>=0,"c")
obj=(x.prod(P,"*","*"))
model.setObjective(obj, GRB.MAXIMIZE)

model.optimize()
for v in model.getVars():
    if v.x >0:
        print("Candidate ",v.varName[2]," took job ",v.varName[4])
print("max profit : ",obj.getValue())