#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

# Example data points
points = [
    {'x': -5, 'y': 1, 'z': -1, 'label': 'Molly'},
    {'x': -1, 'y': 4, 'z': 3, 'label': 'Claire'},
    {'x': 1, 'y': 2, 'z': 4, 'label': 'Rick'},
    {'x': 5, 'y': 5, 'z': 5, 'label': 'Sohla'},
    {'x': 3, 'y': 0, 'z': 2, 'label': 'Gabby'},
    {'x': -2, 'y': -2, 'z': -2, 'label': 'Andy'},
    {'x': -5, 'y': -5, 'z': -5, 'label': 'Brad'},
    {'x': -5, 'y': -5, 'z': 3, 'label': 'Delaney'},
    {'x': 4, 'y': -4, 'z': -3, 'label': 'Chris'},
]

# Create figure and 3D axes
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot points
for point in points:
    ax.scatter(point['x'], point['y'], point['z'], label=point['label'])
    ax.text(
        point['x'] + 0.2,
        point['y'] + 0.2,
        point['z'] + 0.2,
        point['label'])

# Draw dotted black lines along the axes
ax.plot([-5, 5], [0, 0], [0, 0], 'k--')  # X axis
ax.plot([0, 0], [-5, 5], [0, 0], 'k--')  # Y axis
ax.plot([0, 0], [0, 0], [-5, 5], 'k--')  # Z axis

x_label = ax.set_xlabel('influencer ⟸⟹ specialist')
y_label = ax.set_ylabel('dumb ⟸⟹ smart')
z_label = ax.set_zlabel('phony ⟸⟹ sincere')

# Set limits to ensure origin is in the center
ax.set_xlim([-5, 5])
ax.set_ylim([-5, 5])
ax.set_zlim([-5, 5])


def rotate(angle):
    ax.view_init(elev=10, azim=angle)
    # Update axis labels positions
    x_label.set_position((0.5, -0.1))
    y_label.set_position((-0.1, 0.5))
    z_label.set_position((0.1, 0.5))

    x_label.set_rotation(angle)
    y_label.set_rotation(angle)
    z_label.set_rotation(angle)


ani = animation.FuncAnimation(
    fig, rotate, frames=np.arange(0, 360, 1), interval=50)
ani.save('ba-alignment.mp4', writer='ffmpeg', fps=20)

plt.show()
