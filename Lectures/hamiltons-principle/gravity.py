import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Constants and initial conditions
G = 1.0       # Gravitational constant (choose units)
M = 2.0       # Central mass
m = 1.0       # Orbiting mass (can set m=1 for simplicity)
r0 = np.array([1.0, 0.0])  # Initial position
v0 = np.array([0.0, 1.0])  # Initial velocity (adjust for orbit shape)

def gravity_equations(t, y):
    x, y_pos, vx, vy = y
    r = np.sqrt(x**2 + y_pos**2)
    ax = -G * M * x / r**3
    ay = -G * M * y_pos / r**3
    return [vx, vy, ax, ay]

# Time span and initial state
t_span = (0, 20)
y0 = np.array([r0[0], r0[1], v0[0], v0[1]])

# Solve ODE
sol = solve_ivp(gravity_equations, t_span, y0, 
                t_eval=np.linspace(*t_span, 250),
                rtol=1e-9, atol=1e-12)

x = sol.y[0]
y = sol.y[1]
# Plot orbit
plt.figure(figsize=(6,6))
for i in range(len(x)):
    if i < 500:
        plt.plot(x[i], y[i], marker='.')

    plt.plot(0, 0, 'yo', label='Central Mass', markersize=20)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axis('equal')
    plt.title('Orbital motion under gravity')
    plt.savefig(f'gravity/iter{i}.png', dpi=300)
plt.close()
