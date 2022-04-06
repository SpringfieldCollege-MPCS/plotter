import matplotlib.pyplot as plt

def plotter(x, y):

    ax = plt.scatter(x, y)
    plt.axis("equal")
    plt.show()


if __name__ == "__main__":
    plotter([1, 2, 3], [2, 4, 9])