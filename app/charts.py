import matplotlib.pyplot as plt


def generate_bar_chart(name, labels, values):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.savefig(f'./imgs/{name}.png')
    plt.close()


def generate_pie_chart(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    ax.axis('equal')
    plt.savefig('pie.png')
    plt.close()


if __name__ == '__main__':
    labels = ['a', 'b', 'c']
    values = [10, 40, 800]
    generate_pie_chart(labels, values)
    # generate_bar_chart(labels, values)

# A continuacion esta el codigo de otras graficas.

""" import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 20, 100)
plt.plot(x, np.sin(x))
plt.show() """


""" import matplotlib.pyplot as plt
import math
angle = [math.radians(i) for i in range(0, 360)]
x = [(1 + math.cos(i)) * math.cos(i) for i in angle]
# r = [1+math.cos(i) for i in x]
y = [(1 + math.cos(i)) * math.sin(i) for i in angle]
# print(x,y)

fig, ax = plt.subplots()  # Create a figure containing a single axes.
ax.plot(x, y)  # Plot some data on the axes
plt.show()
 """
