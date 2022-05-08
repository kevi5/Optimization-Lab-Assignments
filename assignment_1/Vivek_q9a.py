import gurobipy as gp
from gurobipy import GRB

Person = ["A", "B"]
Chores = ["c1", "c2", "c3", "c4"]
Time = {("A","c1"):4.5,("A","c2"):7.8,("A","c3"):3.6,
("A","c4"):2.9,("B","c1"):4.9,("B","c2"):7.2,
("B","c3"):4.3,("B","c4"):3.1}

model = gp.Model()

x = model.addVars(Person, Chores, vtype=GRB.BINARY, name="x")

for i in Person:
    model.addConstr(x.sum(i,"*") <= 2, name=f"lazy[{i}]")

for j in Chores:
    model.addConstr(x.sum("*", j) >= 1, name=f"all[{j}]")

model.setObjective(x.prod(Time), GRB.MINIMIZE)

model.optimize()
print('Total Time = ' + str(model.ObjVal))
vals = { k : v.X for k,v in x.items() }
seperate_time={"A":0,"B":0}
for k,v in x.items():
    if v.X==1:
        print(k[0]+" did chore "+k[1])
        seperate_time[k[0]]+=Time[(k[0],k[1])]
for i in Person:
    print(str(i)+ " spend "+str(seperate_time[i]))