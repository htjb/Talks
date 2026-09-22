import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_bvp

# Parameters
m = 1.0         # mass
omega = 1.0     # angular frequency
t0, t1 = 0.0, 5.0
x0, x1 = 1.0, 0.0  # boundary conditions
N = 200
t = np.linspace(t0, t1, N)
dt = t[1] - t[0]

# Solve the true path with scipy.integrate.solve_bvp
def SHO_ODE(t, y):
    return np.vstack((y[1], -omega**2 * y[0]))  # dx/dt = y[1], d²x/dt² = -ω²x

def bc(ya, yb):
    return np.array([ya[0] - x0, yb[0] - x1])

# Initial guess for x(t) and v(t)
y_guess = np.vstack((np.linspace(x0, x1, t.size), np.zeros(t.size)))

sol = solve_bvp(SHO_ODE, bc, t, y_guess)
x_true = sol.sol(t)[0]

# Lagrangian
def L(x, v):
    T = 0.5 * m * v**2          # kinetic energy
    V = 0.5 * m * omega**2 * x**2  # potential energy
    return T - V

# Action integral
def compute_action(x):
    v = np.gradient(x, dt)
    return np.sum(L(x, v)) * dt

# Trial paths: perturbations
epsilons = np.random.uniform(-1, 1, 100)
actions = []
for eps in epsilons:
    perturbation = eps * np.sin(np.pi * (t - t0) / (t1 - t0))
    x_trial = x_true + perturbation
    S = compute_action(x_trial)
    actions.append(S)

# Plot
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
for eps in epsilons[::5]:
    perturbation = eps * np.sin(np.pi * (t - t0) / (t1 - t0))
    x_trial = x_true + perturbation
    plt.plot(t, x_trial, label=f"$\\epsilon={eps:.2f}$")
plt.plot(t, x_true, 'k-', linewidth=2, label="True path")
plt.title("Trial paths and true path")
plt.xlabel("Time")
plt.ylabel("x(t)")
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(epsilons, actions, 'o')
plt.title("Action $S$ vs perturbation $\epsilon$")
plt.xlabel("$\epsilon$")
plt.ylabel("Action $S$")

plt.tight_layout()
plt.show()
