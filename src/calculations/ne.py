import logging
import numpy as np
import random

from src.messages import MESSAGES


def normal_equation(matrix_x, matrix_y):
    thetas = []
    x_transposed = transpose_matrix(matrix_x)
    m_to_invert = multiply_matrixes(matrix_x, matrix_x)
    m_inverted = np.linalg.inv(m_to_invert)
    x_calcs = multiply_matrixes(m_inverted, x_transposed)
    thetas = multiply_matrixes(x_calcs, matrix_y)
    return thetas


def transpose_matrix(m):
    return np.array([[m[j][i] for j in range(len(m))] for i in range(len(m[0]))])


def multiply_matrixes(m1, m2):
    res = []
    m1 = m1.T
    m2 = m2.T
    for ind1, l1 in enumerate(m1):
        row = []
        for ind2, l2 in enumerate(m2):
            row.append(multiply_lists(l1, l2))
        res.append(row)
    res = np.array(res)
    return res


def multiply_lists(l1, l2):
    res = 0
    for ind, val in enumerate(l1):
        res += val * l2[ind]
    return res


def initialize_thetas(input_example):
    thetas = []
    for i in range(0, len(input_example)):
        thetas.append(random.randint(0, 5))
    thetas = np.array(thetas)
    return thetas
