import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Total , N.
N = 1000
# Initial volume of polluted water 
I0 = 100
# Everyone else, S0, is susceptible to infection initially.
S0 = N - I0
# all rates (in 1/months).
k , v = -0.05,0 

# A grid of time points (in months)
t = np.linspace(0, 120, 120)

# define beta
C0,C,D0,r = 0.5,1, 0.05,0.01
# The SIR model differential equations.
def deriv(y, t, N, k,C0,C,D0,r):
    S, I = y
    beta = C0 *(C/(1+(C-D0)*np.exp(-r*t)/D0))
    dSdt = -k*S- beta * I* (1- I/ N) + 0
    dIdt = k*S+ beta * I* (1- I/ N)
    return dSdt, dIdt

# Initial conditions vector
y0 = S0, I0
# Integrate the SIR equations over the time grid, t.
ret = odeint(deriv, y0, t, args=(N,k,C0,C,D0,r))
S, I = ret.T

# Plot the data on three separate curves for S(t), I(t) and R(t)
f1 = plt.figure()
plt.plot(t, I, 'r-', label='Infected')
plt.plot(t, S, 'b-', label='Susceptible')
plt.grid()
plt.legend(loc='best')
plt.xlabel('time')
plt.ylabel('Numbers')
plt.title('Trial')
plt.show()
f1.savefig('S.png')
lt.show()
