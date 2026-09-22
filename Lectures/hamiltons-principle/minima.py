import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.size'] = 14

epsilons = np.linspace(-1, 1, 100)
S_values = epsilons**2 

# Plot
fig, axes = plt.subplots(1, 2, figsize=(10, 5))
axes[0].plot(epsilons, S_values, label=r'$S[x+\epsilon\eta]$')
axes[1].plot(epsilons, -S_values + S_values.max(), label=r'$S[x+\epsilon\eta]$')
for i in range(2):
    axes[i].axvline(0, color='k', linestyle='--', label=r'$\epsilon=0$')
    axes[i].set_xlabel(r'$\epsilon$ (perturbation size)')
    axes[i].grid()
    axes[i].set_xticks([])
    axes[i].set_yticks([])
axes[0].set_ylabel(r'Action $S$')

plt.legend()
plt.tight_layout()
plt.savefig('minima_1d.png', dpi=300)
plt.show()

eps1 = np.linspace(-1, 1, 50)
eps2 = np.linspace(-1, 1, 50)
E1, E2 = np.meshgrid(eps1, eps2)
S_saddle = E1**2 - E2**2


fig = plt.figure(figsize=(5, 5))
ax2 = fig.add_subplot(1, 1, 1, projection='3d')
ax2.plot_surface(E1, E2, S_saddle, cmap='coolwarm', alpha=0.8, edgecolor='k')
ax2.set_xlabel(r'$\epsilon_1$')
ax2.set_ylabel(r'$\epsilon_2$')
ax2.set_zlabel(r'Action $S$')
ax2.view_init(elev=30, azim=30)

ax2.set_xticks([])
ax2.set_yticks([])
ax2.set_zticks([])

plt.tight_layout()
plt.savefig('saddle_point_2d.png', dpi=300)
plt.show()
