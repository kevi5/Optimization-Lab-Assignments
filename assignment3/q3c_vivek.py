import gurobipy as gp
from gurobipy import GRB

C=["1","2","3"]
J=["4","5","6"]
P={("1","4"):2,("2","4"):3,("2","6"):2,("3","4"):1,("3","5"):1}
JC=["1","2","3","4","5","6"]
model = gp.Model()
y = model.addVars(JC,vtype=GRB.INTEGER ,name="y")
for i in C:
    model.addConstr(y[i]>=0,"c1[{i}]")
    for j in J:
        model.addConstr(y[j]>=0,"c1[{j}]")
        try:
            # print(P[i,j])
            model.addConstr(
                y[i]+y[j]>=P[i,j],name=f"c[{i},{j}]"
            )
        except:
            pass
obj=(y.sum("*"))
model.setObjective(obj, GRB.MINIMIZE)

model.optimize()
for v in model.getVars():
    print("Value of y",v.varName[2],"is",abs(v.x))
print("min sum : ",obj.getValue())