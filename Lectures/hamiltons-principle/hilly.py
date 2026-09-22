import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_bvp
from noise import pnoise2  # Perlin noise for realistic terrain

# --- Realistic "mountain range" potential ---
def V(x, y, scale=0.03, octaves=4, persistence=0.5, lacunarity=2.0):
    # Works for scalar or array inputs
    return np.array([
        pnoise2(
            xi * scale, yi * scale,
            octaves=octaves,
            persistence=persistence,
            lacunarity=lacunarity,
            repeatx=1024, repeaty=1024, base=21
        )
        for xi, yi in np.broadcast(x, y)
    ]).reshape(np.shape(x)) * 200

# Generate terrain for plotting
grid_x, grid_y = np.meshgrid(np.linspace(-15, 20, 600), np.linspace(0, 20, 600))
Z = V(grid_x, grid_y)

# Plot
plt.figure(figsize=(10, 8))
plt.contour(grid_x, grid_y, Z, levels=40, cmap='Greys_r')
plt.imshow(Z, extent=(-15, 20, 0, 20), origin='lower', cmap='Blues', aspect='auto')
#plt.colorbar(label="Elevation")
plt.axis('off')
plt.savefig('mountain_range_potential.png', dpi=300, bbox_inches='tight')
plt.show()
