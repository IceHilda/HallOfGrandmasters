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
kill_rate = 0.01

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

# A collection of lists to track patients over time
tally = {
    "healthy": [gridsize**2 - 1],
    "sickos": [1],
    "immune": [0],
    "dead": [0],
    "cured": [0],
    "time": [0]
    }



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
    """
    Perform actions on all infected members of the population in a random order
    """
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
    # Re-count everything
    add_tally(grid)
    return grid


def add_tally(grid):
    """
    Count up the number of
    :param grid:
    :return:
    """
    # Count number of each patient type in the grid
    tally['healthy'].append(len(grid[grid == 0]))
    tally['sickos'].append(len(grid[grid == 1]))
    tally['immune'].append(len(grid[grid == -1]))
    tally['dead'].append(len(grid[grid == 2]))
    tally['time'].append(tally['time'][-1]+1)


def show_summary():
    print(f"Ended at day {tally['time'][-1]} with: \n"
          f"{len(grid[grid == 0])} never infected,\n"
          f"{len(grid[grid == -1])} cured,\n"
          f"{len(grid[grid == 2])} killed.")
    max_idx = tally['sickos'].index(max(tally['sickos']))
    print(f"Disease peaked at day {tally['time'][max_idx]} with {max(tally['sickos'])} infected.")

# Unreadable figure setup bullshit
fig, (ax1, ax2) = plt.subplots(2, 1, gridspec_kw={'height_ratios': [5, 1]})
fig.set_figheight(8)
fig.set_figwidth(6)
cmap = colors.ListedColormap(['green', 'lightblue', 'red', 'black'])
boundaries = [-1, 0, 1, 2, 3]
norm = colors.BoundaryNorm(boundaries, cmap.N, clip=True)
p1 = ax1.imshow(grid, cmap=cmap, norm=norm, animated=True)
#p2 = ax2.plot(tally(grid), 'r')
p2, = ax2.plot(tally['time'], tally['sickos'], 'r', animated=True)
p3, = ax2.plot(tally['time'], tally['immune'], 'g', animated=True)
p4, = ax2.plot(tally['time'], tally['dead'], 'k', animated=True)
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
    p2.set_data(tally['time'], tally['sickos'])
    p3.set_data(tally['time'], tally['immune'])
    p4.set_data(tally['time'], tally['dead'])
    ax2.set_xlim(0, max(tally['time']))
    # ax2.set_ylim(0, max(max(sickos), max(immune)))
    # End sim if the disease is gone
    if tally['sickos'][-1] == 0:
        ani.event_source.stop()
        show_summary()
    return p1, p2, p3, p4,


ani = animation.FuncAnimation(fig, updatefig, interval=5, blit=True)  # , fargs=(p1, p2)
plt.show()



# plotobject.set_data(grid)
# plt.draw()

