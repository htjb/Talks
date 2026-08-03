
import numpy as np
import matplotlib.pyplot as plt

# Using astronomical units for much nicer numbers
AU = 1.496e11  # meters
M_sun = 1.989e30  # kg
year = 365.25 * 24 * 3600  # seconds

# Method 1: Astronomical units
x_au = np.linspace(-1.1, 1.1, 100)  # position in AU
y_au = np.linspace(-1.1, 1.1, 100)  # position in AU
M = 1.0  # Solar masses
m = 3.0e-6  # Earth masses in solar masses (6e24 kg / 2e30 kg)
G_au = 39.5  # AU³/(M_sun * year²)

X_au, Y_au = np.meshgrid(x_au, y_au)
# Avoid division by zero at origin
r_au = np.sqrt(X_au**2 + Y_au**2)
r_au[r_au == 0] = 1e-10
V_au = -G_au * M / r_au

plt.figure(figsize=(5, 4))

plt.imshow(V_au, extent=(-1.1, 1.1, -1.1, 1.1),
           origin='lower', cmap='Blues', aspect='auto',
           vmin=-200, vmax=0)
cbar = plt.colorbar(label='Gravitational Potential (AU²/year²)')

# Get current ticks and modify the bottom one
ticks = cbar.get_ticks()
tick_labels = [f'{tick:.0f}' for tick in ticks]
tick_labels[0] = '<-200'  # Replace the first (bottom) tick label

cbar.set_ticks(ticks)
cbar.set_ticklabels(tick_labels)
plt.xlabel('X Position (AU)')
plt.ylabel('Y Position (AU)')
plt.xticks([1.0, 0.0, -1.0])
plt.yticks([1.0, 0.0, -1.0])

plt.savefig("gravitational_potential_au.png", dpi=300)
plt.show()