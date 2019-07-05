import csv
import numpy as np


def obtain_gd_input(input_file):
    with open(input_file) as csv_file:
        file = csv.reader(csv_file, delimiter="\t")
        matrix = []
        for ind, z in enumerate(file):
            if ind == 0:
                continue
            z[:5] = map(float, z[0:5])
            matrix.append(z)
    matrix = np.array([np.array(xi) for xi in matrix])
    return matrix


def obtain_ne_input(input_file):
    with open(input_file) as csv_file:
        file = csv.reader(csv_file, delimiter="\t")
        matrix_x = []
        matrix_y = []
        for ind, z in enumerate(file):
            if ind == 0:
                continue
            to_append_m1 = [1.0]
            to_append_m1.extend(list(map(float, z[0:-1])))
            matrix_x.append(to_append_m1)
            matrix_y.append([float(z[-1])])
    matrix_x = np.array([np.array(xi) for xi in matrix_x])
    matrix_y = np.array([np.array(xi) for xi in matrix_y])
    return matrix_x, matrix_y
