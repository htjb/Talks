import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as colors

plt.rcParams['font.size'] = 15
# parameters
m = 1.0
t0, t1 = 0.0, 1.0
x0, x1 = 0.0, 1.0
N = 100
t = np.linspace(t0, t1, N)
dt = t[1] - t[0]

# true path (free particle: linear interpolation)
x_true = x0 + (x1 - x0) * (t - t0) / (t1 - t0)

# Lagrangian
def L(x, v):
    return 0.5 * m * v**2  # free particle: V(x)=0

# Action integral
def compute_action(x):
    v = np.gradient(x, dt)
    return np.sum(L(x, v)) * dt


# Trial paths: perturbations
epsilons = np.random.uniform(-1, 1, 100)
actions, trials = [], []
for eps in epsilons:
    perturbation = eps * np.sin(np.pi * (t - t0) / (t1 - t0))
    x_trial = x_true + perturbation
    S = compute_action(x_trial)
    actions.append(S)
    trials.append(x_trial)

actions = np.array(actions)

norm = colors.Normalize(vmin=actions.min(), vmax=actions.max())
cmap = plt.get_cmap('viridis')
sm = cm.ScalarMappable(norm=norm, cmap=cmap)

plt.figure(figsize=(6, 5))
for i in range(len(trials)):
    plt.plot(t, trials[i],
        color=sm.to_rgba(actions[i]))
    plt.plot(t, x_true, c='r', ls='--', linewidth=2, label="True path")
    plt.title("Trial paths and true path")
    if i == 0:
        plt.colorbar(sm, label=r'$S$')
    plt.tight_layout()
    plt.xlabel(r'$t$')
    plt.ylabel(r'$x$')
    plt.xlim([-0.1, 1.1])
    plt.ylim([-1, 2])
    plt.savefig(f'free-particle-paths/trial{i}.png', dpi=300, bbox_inches='tight')
plt.close()
