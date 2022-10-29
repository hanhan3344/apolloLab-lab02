from matplotlib.lines import lineStyles
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as cm

from matplotlib.collections import LineCollection
from matplotlib.colors import ListedColormap

fig, ax = plt.subplots()

def draw_line(total_line, has_color=True):
    i = 0
    g = 0
    c_list = list(cm.TABLEAU_COLORS.keys())
    style_list = ['solid', 'dashed', 'dashot', 'dotted']
    l_list = ['apollo/canbus/chassis/speed_mps', 'apollo/canbus/chassis/throttle_percentage', 'apollo/canbus/chassis/brake_percentage', 'apollo/canbus/chassis/steering_percentage',
              'apollo/control/throttle', 'apollo/control/brake', 'apollo/control/steering_rate', 'apollo/control/steering_target']

    lines = []
    for module in total_line:
        # print(module)
        
        for line in module:
            i += 1
            x = [point.x for point in line]
            y = [point.y for point in line]

            points = np.array([x, y]).T.reshape(-1, 1, 2)
            segments = np.concatenate([points[:-1], points[1:]], axis=1)

            lc = LineCollection(segments, linewidths=1, colors=c_list[i], linestyles=style_list[g])
            lines.append(lc)
            ax.add_collection(lc)
        g += 1

    ax.legend(handles=lines, labels=l_list)
    ax.autoscale()

def show():
    # show map
    plt.show()