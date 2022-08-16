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

    
    x = [-1, 12]
    y = [1, 5]

    plt.scatter(x, y, marker='o')

    ax.set_xlim(-15, 15)
    ax.set_ylim(-10, 20)
    ax.set_aspect('equal')

    plt.show()
    return plt

p = plt_draw()
p.show()


