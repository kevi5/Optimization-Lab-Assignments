import gurobipy as gp
from gurobipy import GRB

y=["1","2","3","4","5","6","7"]
model=gp.Model()
y=model.addVars(y,name="y")
model.addConstr(11*y["1"]+3*y["2"]+y["3"]>=13,"c1")
model.addConstr(53*y["1"]+6*y["2"]+y["4"]>=16,"c2")
model.addConstr(5*y["1"]+5*y["2"]+y["5"]>=16,"c3")
model.addConstr(5*y["1"]+1*y["2"]+y["6"]>=14,"c4")
model.addConstr(29*y["1"]+34*y["2"]+y["7"]>=39,"c5")

# for i in x:
#     model.addConstr(x[i]>=0,"c2[{i}]")
#     model.addConstr(x[i]<=1,"c3[{i}]")
obj=40*y["1"]+20*y["2"]+y["3"]+y["4"]+y["5"]+y["6"]+y["7"]
model.setObjective(obj, GRB.MINIMIZE)
model.optimize()
print("min : ",obj.getValue())
for v in model.getVars():
    print(v.varName,v.x)
shadow_price = model.getAttr(GRB.Attr.Pi)
print(shadow_price)