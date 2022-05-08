import numpy as np
import matplotlib.pyplot as plt
import math

def zeroth_order(x1):
    return  x1**5 + 5*math.exp(-3*x1)

def first_order(x1,x0):
    return x1**5 + 5*math.exp(-3*x1) + x0*(5*(x1**4)-15*np.exp(-3*x1))

def second_order(x1,x0):
    return x1**5 + 5*math.exp(-3*x1) + x0*(5*(x1**4)-15*np.exp(-3*x1))+(x0*x0/2)*(20*(x1**3)+45*np.exp(-3*x1))

x0=np.arange(-0.5,0.5,0.001)
nrow = 1; ncol = 2;
fig, axs = plt.subplots(nrows=nrow, ncols=ncol)
x=[1,2]
for i in range(2):
    # zeroth_order1=zeroth_order(x[i])*np.ones(x0.shape)
    zeroth_order1=np.full(x0.shape,zeroth_order(x[i]))
    x_1=x0+x[i]
    axs[i].plot(x_1 , (x_1)**5 + 5*np.exp(-3*(x_1)),color='black')
    axs[i].plot(x[i] + x0, zeroth_order1, label = 'Zeroth Order')
    axs[i].plot(x[i] + x0, first_order(x[i],x0), label = 'First order')
    axs[i].plot(x[i] + x0, second_order(x[i],x0), label = 'Second order')
    axs[i].set_title('X0 = '+str(x[i]))
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()



