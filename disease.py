"""
Simple simulation showing the spread of disease
0: Healthy
1: Infected
2: Dead
-1: Immune (healed)
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.colors as colors


gridsize = 100

# Basic sim
infect_rate = 0.1
heal_rate = 0.01
kill_rate = 0.02

# Common cold
# infect_rate = 0.02
# heal_rate = 0.02
# kill_rate = 0.002

# Ebola
# infect_rate = 0.1
# heal_rate = 0.01
# kill_rate = 0.2

grid = np.zeros((gridsize, gridsize))

# Create patient zero
grid[np.random.randint(0, gridsize), np.random.randint(0, gridsize)] = 1

sickos = [1]
immune = [0]
t = [0]


def infect(r, c):
    """
    Look at each neighbor of a point and, if healthy, have chance to infect
    :param r:
    :param c:
    :return:
    """
    for nr in np.arange(-1, 2):
        for nc in np.arange(-1, 2):
            try:
                if grid[r+nr, c+nc] == 0:
                    grid[r+nr, c+nc] = np.random.binomial(1, infect_rate)
            except IndexError:  # Out of bounds, ignore
                pass


def turn(grid):
    # Select infected people
    rows, cols = np.where(grid == 1)
    #print(f"Infected at {rows}, {cols}")
    # In random order, go through each infected
    idx = np.arange(len(rows))
    np.random.shuffle(idx)
    for i in idx:
        # Chance to heal
        if np.random.binomial(1, heal_rate):
            grid[rows[i], cols[i]] = -1
        # Chance to die
        if np.random.binomial(1, kill_rate):
            grid[rows[i], cols[i]] = 2
        # chance to infect
        else:
            infect(rows[i], cols[i])
    return grid


def tally(grid):
    # Count number of infected people in the grid
    current_sickos = len(grid[grid == 1])
    current_immune = len(grid[grid == -1])

    sickos.append(current_sickos)
    immune.append(current_immune)
    t.append(t[-1]+1)


# Unreadable figure setup bullshit
fig, (ax1, ax2) = plt.subplots(2, 1, gridspec_kw={'height_ratios': [5, 1]})
fig.set_figheight(8)
fig.set_figwidth(6)
cmap = colors.ListedColormap(['green', 'lightblue', 'red', 'black'])
boundaries = [-1, 0, 1, 2, 3]
norm = colors.BoundaryNorm(boundaries, cmap.N, clip=True)
p1 = ax1.imshow(grid, cmap=cmap, norm=norm, animated=True)
#p2 = ax2.plot(tally(grid), 'r')
p2, = ax2.plot(t, sickos, 'r', animated=True)
p3, = ax2.plot(t, immune, 'g', animated=True)
ax2.set_ylim(0, gridsize**2)
ax1.xaxis.set_visible(False)
ax1.yaxis.set_visible(False)
ax2.xaxis.set_visible(False)
ax2.yaxis.tick_right()
ax2.yaxis.set_ticks_position('both')
#ax2.yaxis.set_visible(False)


def updatefig(*args):
    """
    Function that's called automatically by the animation loop
    """
    p1.set_array(turn(grid))
    tally(grid)
    p2.set_data(t, sickos)
    p3.set_data(t, immune)
    ax2.set_xlim(0, max(t))
   # ax2.set_ylim(0, max(max(sickos), max(immune)))
    # End sim if the disease is gone
    if sickos[-1] == 0:
        ani.event_source.stop()
    return p1, p2, p3,


ani = animation.FuncAnimation(fig, updatefig, interval=5, blit=True)  # , fargs=(p1, p2)
plt.show()

# plotobject.set_data(grid)
# plt.draw()

