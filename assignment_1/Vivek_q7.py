import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn-poster')

def f(x):
    return (x**5)+5*np.exp(-3*x)

def taylor0(x0,h):
    return f(x0)+0*h

def taylor1(x0,h):
    return taylor0(x0,h)+h*(5*(x0**4)-15*np.exp(-3*x0))

def taylor2(x0,h):
    return taylor1(x0,h)+(h*h/2)*(20*(x0**3)+45*np.exp(-3*x0))

h=np.linspace(-1,1,50)
x0_1=1
x0_2=2
t_0=taylor0(x0_1,h)
t_1=taylor1(x0_1,h)
t_2=taylor2(x0_1,h)
t2_0=taylor0(x0_2,h)
t2_1=taylor1(x0_2,h)
t2_2=taylor2(x0_2,h)
fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.plot(x0_1+h, t_0, label = 'zero_order')
ax1.plot(x0_1+h, t_1, label = 'first_order')
ax1.plot(x0_1+h, t_2, label = 'second_order')
ax1.plot(x0_1+h, f(x0_1+h), label = 'original')
ax1.set_title('Taylor Series Approximations for x0=1',fontsize = 10)
ax2.plot(x0_2+h, t2_0, label = 'zero_order')
ax2.plot(x0_2+h, t2_1, label = 'first_order')
ax2.plot(x0_2+h, t2_2, label = 'second_order')
ax2.plot(x0_2+h, f(x0_2+h), label = 'original')
ax2.set_title('Taylor Series Approximations for x0=2',fontsize = 10)
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()



