import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import Circle
import matplotlib.patches as mpatches

# Set up the 3D figure
fig = plt.figure(figsize=(15, 10), )
ax = fig.add_subplot(111, projection='3d', computed_zorder=False)

# Parameters
slope_angle = 25  # degrees
slope_length = 10
slope_width = 6
ball_radius = 0.3
g = 9.81

# Create the slope surface
x_slope = np.linspace(0, slope_length, 50)
y_slope = np.linspace(-slope_width/2, slope_width/2, 30)
X_slope, Y_slope = np.meshgrid(x_slope, y_slope)
Z_slope = (slope_length - X_slope) * np.tan(np.radians(slope_angle))

# Plot the slope surface
ax.plot_surface(X_slope, Y_slope, Z_slope, alpha=0.7, color='lightgray',
                linewidth=0.5, edgecolor='gray', zorder=2)

# Ball trajectory parameters
# Ball rolls straight down the middle of the slope
t_total = np.sqrt(14 * slope_length / (5 * g * np.sin(np.radians(slope_angle))))
t = np.linspace(0, t_total, 100)

# Position along slope (straight down the middle)
s = (5/14) * g * np.sin(np.radians(slope_angle)) * t**2
x_ball = s
y_ball = np.zeros_like(s)  # Rolling down the center

# Fixed: Ball sits on the shifted surface
surface_height = (slope_length - s) * np.tan(np.radians(slope_angle)) - 0.5
z_ball = surface_height + ball_radius

# Show ball at several positions along the path
pos = 40
colors = 'red'

x_center = x_ball[pos]
y_center = y_ball[pos]
z_center = z_ball[pos]

# Create sphere for ball
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
u, v = np.meshgrid(u, v)  # meshgrid for proper parametric surface

x_sphere = ball_radius * np.sin(v) * np.cos(u) + x_center
y_sphere = ball_radius * np.sin(v) * np.sin(u) + y_center
z_sphere = ball_radius * np.cos(v) + z_center

# Plot the ball
ax.plot_surface(x_sphere, y_sphere, z_sphere, color=colors, zorder=10,
                rstride=1, cstride=1, linewidth=0, antialiased=True)

# Add a vertical face on the +y side (to make it a wedge)
Y_side1 = slope_width / 2  # y = +width/2
X_side1 = np.array([[0, slope_length],
                    [0, slope_length]])
Z_side1 = np.array([[0, 0],
                    [slope_length * np.tan(np.radians(slope_angle)), 0]])
Y_side1 = np.full_like(X_side1, Y_side1)
ax.plot_surface(X_side1, Y_side1, Z_side1, color='lightgray', alpha=0.7)

# Add a vertical face on the -y side (to make it a wedge)
Y_side2 = -slope_width / 2
X_side2 = X_side1.copy()
Z_side2 = Z_side1.copy()
Y_side2 = np.full_like(X_side2, Y_side2)
ax.plot_surface(X_side2, Y_side2, Z_side2, color='lightgray', alpha=0.7)

# Add the base under the slope
X_base, Y_base = np.meshgrid(x_slope, y_slope)
Z_base = np.zeros_like(X_base)  # flat ground
ax.plot_surface(X_base, Y_base, Z_base, color='lightgray', alpha=0.5)

# Set axis limits for better view
ax.set_xlim(0, slope_length)
ax.set_ylim(-slope_width/2, slope_width/2)
ax.set_zlim(0, slope_length * np.tan(np.radians(slope_angle)) + 2)
ax.axis('off')

# Set viewing angle
ax.view_init(elev=10, azim=45)

plt.tight_layout()
plt.savefig('ball_3d_slope.png', dpi=300, bbox_inches='tight')
plt.close()

# Print some physics info
print("3D Ball Rolling Physics:")
print("=" * 30)
print(f"Slope angle: {slope_angle}°")
print(f"Slope length: {slope_length}m")
print(f"Ball radius: {ball_radius}m")
print(f"Total roll time: {t_total:.2f}s")
print(f"Final speed: {np.sqrt((10/7) * g * slope_length * np.sin(np.radians(slope_angle))):.2f}m/s")
print()
print("The ball rolls straight down the steepest gradient (middle of slope)")
print("Multiple colored spheres show the ball's position at different times")