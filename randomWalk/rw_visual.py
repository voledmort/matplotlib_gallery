import matplotlib.pyplot as plt

from randomWalk.random_walk import RandomWalk

count = 10
while count > 0:
    rw = RandomWalk(num_points=50000)
    rw.fill_walk()

    plt.figure(figsize=(10, 6))

    point_numbers = list(range(rw.num_points))

    plt.scatter(rw.x_values, rw.y_values,
                c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1)

    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1],
                c='r', edgecolors='none', s=100)

    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()
    count -= count


