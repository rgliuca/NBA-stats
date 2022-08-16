import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, Arc
def plt_draw(ax=None, color='black', lw=2, outer_lines=False):
    # If an axes object isn't provided to plot onto, just get current one
    if ax is None:
        ax = plt.gca()

    circle = Circle((0, 0), radius=7.5, linewidth=lw, color=color, fill=False)

    rectangle = Rectangle((-30, -7.5), 60, -1, linewidth=lw, color=color)


    ax.add_patch(circle)
    ax.add_patch(rectangle)

    
    x1, y1 = [-1, 12], [1, 4]
    x2, y2 = [1, 10], [3, 2]

    plt.plot(x1, y1, x2, y2, marker='o')

    plt.show()
    return plt

p = plt_draw()
p.show()
