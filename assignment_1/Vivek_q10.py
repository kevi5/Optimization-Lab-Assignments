import gurobipy as gp
from gurobipy import GRB

#input total no. of nodes
print("Total no. of nodes")
n=int(input())
Nodes=[]
#rest of nodes are in form of A,B,C...
for i in range(n):
    Nodes.append(chr(ord("A")+i))
print(Nodes)
print("Input Start Node and End Node from following nodes in form S,E")
a=input()
(S,E)=tuple(str(x) for x in a.split(","))
t=(n-1)*(n)/2
j=0
print("Tota no. of edges:")
m=int(input())
c={}
arg={}
print("Give edges in form of A,B:cij")
for j in range(m):
    a=input()
    temp=a.split(":")
    c[tuple(str(x) for x in temp[0].split(","))]=int(temp[1])
    arg[tuple(str(x) for x in temp[0].split(","))]=int(temp[1])
# print(c)
# print(S)
m = gp.Model()

x = m.addVars(arg, name = "x")
# print(x)
m.addConstrs(
    (x.sum(i,j) <= c[i,j] for i,j in arg), "cap")
m.addConstrs(
    (x.sum('*',j) - x.sum(j,'*') == 0 for j in Nodes if j != S and j != E))
obj = (x.sum('*', S) - x.sum(S,'*'))
m.setObjective(obj, GRB.MAXIMIZE)

m.optimize()

