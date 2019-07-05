import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from src.settings import default_output_folder


def plot_points(title, training_data, found_result, calculated_value):
    if len(training_data[0]) == 2:
        plt.scatter(calculated_value[0], calculated_value[1], label='obtained output', marker=5)

        x = [item[0] for item in training_data]
        y = [item[1] for item in training_data]
        plt.scatter(x, y, label='training set', marker=6)

        x = []
        y = []
        for t in training_data:
            x.append(t[0])
            y.append(round(found_result[1] * t[0] + found_result[0], 2))
        plt.plot(x, y, label='found line')
    elif len(training_data[0]) == 3:
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        ax.scatter(calculated_value[0],
                   calculated_value[1],
                   calculated_value[2],
                   label='obtained output',
                   marker=5)

        x = [item[0] for item in training_data]
        y = [item[1] for item in training_data]
        z = [item[2] for item in training_data]
        ax.scatter(x, y, z, label='training set', marker=6)

        x = []
        y = []
        z = []
        for t in training_data:
            x.append(t[0])
            y.append(t[1])
            z.append(round(found_result[2] * t[1] + found_result[1] * t[0] + found_result[0], 2))
        ax.plot(x, y, z, label='found line')
    else:
        print("plot not ready")
        return

    plt.title(title.split('/')[1].split('.')[0])

    plt.legend()

    plt.savefig("{}/{}_output.png".format(default_output_folder, title.split('/')[1].split('.')[0]))
