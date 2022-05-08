import gurobipy as gp
from gurobipy import GRB
import math
print("Total no. of candidates n:")
n=int(input())
cand=[]
for i in range(int(n)):
    cand.append(str(i+1))
print("Candidates :",cand)
print("Total no. of Jobs m :")
m=int(input())
job=[]
for i in range(int(m)):
    job.append(str(i+n+1))
print("Jobs :",job)

print("Give edges in form of i,j:pij and type quit when there are less than n*m edges:")
reward={}
for j in range(n*m):
    a=input()
    if a=='quit':
        break
    temp=a.split(":")
    reward[tuple(str(x) for x in temp[0].split(","))]=int(temp[1])
print(reward)
model = gp.Model()
x = model.addVars(cand,job,vtype=GRB.BINARY ,name="x")
for i in cand:
    model.addConstr(x.sum(i,"*")<=1,name=f"cand[{i}]")
for i in job:
    model.addConstr(x.sum("*",i)<=1,name=f"job[{i}]")
obj=(x.prod(reward,"*","*"))
model.setObjective(obj, GRB.MAXIMIZE)

model.optimize()
print("The max possible reward is: ",obj.getValue())
print("The candidate job assignment is as follows:")
for k in model.getVars():
    print(k.varName, k.x)
