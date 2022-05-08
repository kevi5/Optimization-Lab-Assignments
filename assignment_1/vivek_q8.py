import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch

def Z(X1,X2):
    return (1-X1)**2+100*(X2-(X1)**2)**2

def gradient(x,y):
  return (400*(x**3)-400*x*y+2*x-2,200*(y-x**2))

a=np.array([0.5, 2, 5, 10, 50, 100, 200, 400, 800])
x1 = np.linspace(-2,2,100)
x2 = np.linspace(-2,2,100)

[X1, X2] = np.meshgrid(x1, x2)
fig, ax = plt.subplots(1, 1)
z = Z(X1,X2)
# r=100
# f=r + 0 *x1+0*x2
ax.contour(X1,X2, z,[0.5, 2, 5, 10, 50, 100, 200, 400, 800])
# for i in a:
#     z=i+0*X1+0*X2
#     idx=np.argwhere(np.diff(np.sign(Z-z)))
#     x1=X1[idx[0][0]][idx[0][1]]
#     x2=X2[idx[0][0]][idx[0][1]]
#     dx1,dx2=gradient(x1,x2)
#     det=np.sqrt((dx1)**2+(dx2)**2)
#     arrow = FancyArrowPatch((x1, x2), (x1+(dx1/det), x2+(dx2/det)),    
#                             arrowstyle='simple', color='k', mutation_scale=10)
#     ax.add_patch(arrow)
x1=X1[0][40]
x2=X2[50][50]
# x1=x0[0]
# x2=x0[1]
dx1,dx2=gradient(x1,x2)
det=np.sqrt((dx1)**2+(dx2)**2)
arrow = FancyArrowPatch((x1, x2), (x1+(dx1/det), x2+(dx2/det)),    
                        arrowstyle='simple', color='k', mutation_scale=10)
ax.add_patch(arrow)
plt.plot([x1],[x2],marker='o',markersize=10, color ='r')
# ax.plot(x1,x2,f)
ax.set_title('Contour Plot')
ax.set_xlabel('feature_x1')
ax.set_ylabel('feature_x2')

print(plt.show())