#!/usr/bin/env python
import click
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as mp3d
import numpy as np

points = [
    {'x': -5, 'y': 1, 'z': -1,
     'label': 'Molly', 'ig_followers': 785,
     },

    {'x': -1, 'y': 4, 'z': 3,
     'label': 'Claire', 'ig_followers': 1000,
     },

    {'x': 1, 'y': 2, 'z': 4,
     'label': 'Rick', 'ig_followers': 234,
     },

    {'x': 5, 'y': 5, 'z': 5,
     'label': 'Sohla', 'ig_followers':  581,
     },

    {'x': 3, 'y': 0, 'z': 2,
     'label': 'Gabby', 'ig_followers': 237
     },

    {'x': -2, 'y': -2, 'z': -2,
     'label': 'Andy', 'ig_followers':  333,
     },

    {'x': -5, 'y': -5, 'z': -5,
     'label': 'Brad', 'ig_followers': 808,
     },

    {'x': -5, 'y': -5, 'z': 3,
     'label': 'Delany', 'ig_followers': 272,
     },

    {'x': 4, 'y': -4, 'z': -3,
     'label': 'Chris', 'ig_followers': 394,
     },

    {'x': 2, 'y': 4, 'z': 3,
     'label': 'Carla', 'ig_followers': 410,
     },
]

minf = min([point['ig_followers'] for point in points])
maxf = max([point['ig_followers'] for point in points])
for p in points:
    p['followers_norm'] = (p['ig_followers'] - minf) / (maxf - minf)

S = 7

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')
ax.xaxis.set_ticks([])
ax.yaxis.set_ticks([])
ax.zaxis.set_ticks([])

xy = np.array([
    (-1, -1, 0),
    (1, -1, 0),
    (1,  1, 0),
    (-1,  1, 0),
]) * S
plane = mp3d.art3d.Poly3DCollection([xy], alpha=0.1, linewidth=1)
plane.set_facecolor((0, 0, 0))
ax.add_collection(plane)

ax.plot([-S, S], [0, 0], [0, 0], '--', alpha=0.2, color='k')
ax.plot([0, 0], [-S, S], [0, 0], '--', alpha=0.2, color='k')
ax.plot([0, 0], [0, 0], [-S, S], '--', alpha=0.2, color='k')

for point in points:
    x, y, z = point['x'], point['y'], point['z']
    ax.scatter(
        x, y, z,
        label=point['label'],
        s=10 + point['followers_norm'] * 100)
    zoffs = -0.7 if z < 0 else 0.2
    ax.text(x + 0.2, y + 0.2, z + zoffs, point['label'])
    ax.plot([x, x], [y, y], [0, z], ':')

x_label = ax.set_xlabel('influencer ⟸⟹ specialist')
y_label = ax.set_ylabel('dumb ⟸⟹ smart')
z_label = ax.set_zlabel('evil ⟸⟹ good')

ax.set_xlim([-S, S])
ax.set_ylim([-S, S])
ax.set_zlim([-S, S])


@click.command()
@click.option('--save', is_flag=True, help='Save the plot to a file.')
def main(save: bool = False):
    if save:
        plt.savefig('plot.png', dpi=1000)
    else:
        plt.show()


if __name__ == '__main__':
    main()
