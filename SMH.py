from matplotlib import pyplot as plt
import numpy as np

g = 9.81
l = 1.
N = 250
tstep = 0.04

omega = np.zeros(N)
theta = np.zeros(N)
t = np.zeros(N)

theta[0] = 0.2

for idx in range(N - 1):
    
    omega[idx + 1] = omega[idx] - (g / l) * theta[idx] * tstep
    theta[idx + 1] = theta[idx] + omega[idx + 1] * tstep
    t[idx + 1] = t[idx] + tstep

plt.figure()

plt.plot(t, theta)
plt.xlabel('t (seconds)')
plt.ylabel(r'$\theta\,$(radians)')

plt.figure()

plt.plot(t, omega)
plt.xlabel('t (seconds)')
plt.ylabel('$\omega\,$ (radians / second)')
plt.show()
