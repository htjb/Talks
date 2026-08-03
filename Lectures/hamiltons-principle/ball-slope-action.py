import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import matplotlib.patches as patches

# Parameters
slope_angle = 30  # degrees
slope_length = 8
ball_radius = 0.1
g = 9.81
m = 1.0  # mass

# Position along slope (0 at top, slope_length at bottom)
positions = np.linspace(0, slope_length, 100)

# Height calculation
heights = slope_length * np.sin(np.radians(slope_angle)) - \
    positions * np.sin(np.radians(slope_angle))

vpush = [0, 2, 4, 6, 8]  # Different initial velocities to simulate
color= ['red', 'blue', 'green', 'orange', 'purple']
for k, v in enumerate(vpush):

    # Set up the figure with subplots
    fig, (ax_main, ax_energy) = plt.subplots(2, 1, figsize=(6, 6),)

    # Main diagram - slope and ball
    #ax_main.set_xlim(-1, 10)
    #ax_main.set_ylim(-1, 6)
    #ax_main.set_aspect('equal')

    # Draw slope
    slope_x = [-0.15, slope_length * np.cos(np.radians(slope_angle))]
    slope_y = [slope_length * np.sin(np.radians(slope_angle)), 0]
    #ax_main.plot(slope_x, slope_y, 'k-', linewidth=3, label='Slope')
    ax_main.fill_between(slope_x, slope_y, 0, color='lightgray', alpha=0.5)

    # Show ball at different positions
    position_indices = [0, 20, 40, 60, 80]

    for i, pos_idx in enumerate(position_indices):
        pos = positions[pos_idx]
        x = pos * np.cos(np.radians(slope_angle))
        y = slope_length * np.sin(np.radians(slope_angle)) - pos * np.sin(np.radians(slope_angle))
        
        if i == 0:
            # Draw ball
            ball = Circle((x, y), ball_radius, color=color[k], 
                    label=f'Position {i+1}' if i == 0 else '', zorder=10)
            ax_main.add_patch(ball)
        
        # Add position labels
        ax_main.text(x, y + ball_radius + 0.3, fr'$t_{i+1}$', 
                    ha='center', va='bottom', fontsize=10, fontweight='bold')

    # add an arrow from p1 down slope
    ax_main.annotate('', xy=(positions[20] * np.cos(np.radians(slope_angle)), 
                            slope_length * np.sin(np.radians(slope_angle)) - positions[20] * np.sin(np.radians(slope_angle))),
                    xytext=(positions[0] * np.cos(np.radians(slope_angle)), 
                            slope_length * np.sin(np.radians(slope_angle)) - positions[0] * np.sin(np.radians(slope_angle))),
                    arrowprops=dict(arrowstyle='->', color='black', lw=1.5))
    ax_main.axis('off')  # Hide axes

    # For rolling sphere: v² = (10/7) * g * h_fallen
    # where h_fallen = positions * sin(theta)
    h_fallen = positions * np.sin(np.radians(slope_angle))
    velocities_squared = (10/7) * g * h_fallen + v**2

    # Energy calculations
    T_trans = 0.5 * m * velocities_squared  # Translational kinetic energy
    T_total = T_trans

    # Set reference potential energy at bottom of slope
    V = m * g * heights  # Potential energy
    L = T_total - V  # Lagrangian

    # Energy bar chart
    #ax_energy.clear()
    positions_sample = [0, 20, 40, 60, 80]
    x_pos = np.arange(len(positions_sample))

    T_sample = [T_total[i] for i in positions_sample]
    V_sample = [V[i] for i in positions_sample]
    L_sample = [L[i] for i in positions_sample]

    ax_energy.plot(x_pos, L_sample, color=color[k], marker='o', linestyle='-', linewidth=2)
    ax_energy.fill_between(x_pos, [0]*len(x_pos), L_sample, color=color[k], alpha=0.3, label=r'$V_\mathrm{push} =$ ' + f'{v}' + r' $\mathrm{m/s}$')
    # area under the curve
    ax_energy.set_ylabel('Lagrangian')
    ax_energy.set_xticks(x_pos)
    ax_energy.set_xticklabels([fr'$t_{i+1}$' for i in range(len(positions_sample))])
    if k == 0:
        ymin, ymax = ax_energy.get_ylim()
    ax_energy.set_ylim(-40, 50)
    ax_energy.legend()
    ax_energy.set_xlabel('Time')
    plt.tight_layout()
    plt.savefig(f'lagrangian_ball_slope_action_{v}.png', dpi=300, bbox_inches='tight')
    plt.show()

# Print some key values for understanding
print("Key Physics Insights:")
print("=" * 50)
print(f"Slope angle: {slope_angle}°")
print(f"Ball mass: {m} kg")
print(f"Ball radius: {ball_radius} m")
print()
print("At different positions:")
for i, pos_idx in enumerate(position_indices):
    pos = positions[pos_idx]
    print(f"Position {i+1}: s = {pos:.1f}m")
    print(f"  Height: {heights[pos_idx]:.2f}m")
    print(f"  Kinetic Energy: {T_total[pos_idx]:.2f}J")
    print(f"  Potential Energy: {V[pos_idx]:.2f}J")
    print(f"  Lagrangian: {L[pos_idx]:.2f}J")