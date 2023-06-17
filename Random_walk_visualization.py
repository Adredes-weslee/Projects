import matplotlib.pyplot as plt
from random_walk import RandomWalk

#initiate either a scatterplot or line randomwalk using the RandomWalk class 
while True:
    walk_type = input("Scatter or Line? (s/l): ").lower()
    
    rw = RandomWalk()
    rw.fill_walk()
    
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15,9))
    point_numbers = range(rw.num_points)

    if walk_type == 's':
        ax.scatter(0, 0, c='green', edgecolors='none', s=100)
        ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
            s=100)
        ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
            edgecolors='none', s=15)
    else:
        ax.scatter(0, 0, c='green', edgecolors='none', s=100)
        ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
            s=100) 
        ax.plot(rw.x_values, rw.y_values,)

    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()

    keep_running = input("Make another walk? (y/n): ").lower()
    if keep_running == 'n':
        break

