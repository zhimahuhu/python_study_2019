import matplotlib.pyplot as plt
from random_walk import RandomWalk

flag = True
while flag:
    rw = RandomWalk(50000)
    rw.fill_walk()
    plt.figure(dpi=128, figsize=(10, 6))
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, s=1, edgecolors='none')
    plt.scatter(0, 0, c='green', s=100, edgecolors='none')
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='yellow', s=100, edgecolors='none')
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    plt.show()
    # keep_running = input('Make another walk? (y/n):')
    # if keep_running == 'n':
    #     break
    flag = False
