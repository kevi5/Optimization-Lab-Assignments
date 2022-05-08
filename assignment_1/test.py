from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plot
import numpy as np


def rosenbrock(x,y):
  return (1-x)**2 + 100* ((y-x**2))**2

def gradient(x,y):
  return (400*(x**3)-400*x*y+2*x-2,200*(y-x**2))

fig = plot.figure()
ax = fig.gca(projection='3d')

x1 = np.linspace(-2,2,100)
x2 = np.linspace(-2,2,100)  

X, Y = np.meshgrid(x1, x2)
Z = rosenbrock(X,Y)

surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm,linewidth=0, antialiased=False)
surf.set_label('Rosenbrock Function')
a=np.array([0.5, 2, 5, 10, 50, 100, 200, 400, 800])
# z=400+0*X+0*Y
# idx=np.argwhere(np.diff(np.sign(Z-z))).flatten()
for i in a:
  z=i+0*X+0*Y
  idx=np.argwhere(np.diff(np.sign(Z-z)))
  j=idx[0]
  x1=X[j[0]][j[1]]
  y1=Y[j[0]][j[1]]
  z1=Z[j[0]][j[1]]
  dx,dy=gradient(x1,y1)
  h=0.0001
  dx*=h
  dy*=h
  z_1=rosenbrock(x1+dx,y1+dy)
  # print(x1,y1,z1,x1+dx,y1+dy,z_1,'\n')
  ax.quiver( x1,y1,z1,x1+dx,y1+dy,z_1,normalize=True,color='black')
  # j=0
  # while(j<len(idx)):
  # x1=X[idx[j]][idx[j+1]]
  # y1=Y[idx[j]][idx[j+1]]
  # dx,dy=gradient(x1,y1)
  # ax.add_patch(arrow)
  # j=j+2
  ax.plot_wireframe(X,Y,z)
# dx,dy=gradient(X,Y)
# ax.quiver(X,Y,dx,dy)
fig.colorbar(surf, shrink=0.5, aspect=10)
# a=X[1][44]
# b=Y[1][44]
# print(rosenbrock(a,b))
ax.set_xlabel("X1")
ax.set_ylabel("X2")
ax.set_zlabel('f(X1,X2)')

plot.show()