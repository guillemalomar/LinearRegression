import matplotlib.pyplot as plt


def plot_points(title, training_data, found_result):

    x = [item[0] for item in training_data]
    y = [item[1] for item in training_data]
    plt.scatter(x, y, label='training set', marker=1)

    x = []
    y = []
    for t in training_data:
        x.append(t[0])
        y.append(round(found_result[1] * t[0] + found_result[0], 2))
    plt.scatter(x, y, label='found line')

    plt.title(title)

    plt.legend()

    plt.savefig("../output/{}_output.png".format(title.split('/')[2].split('.')[0]))
