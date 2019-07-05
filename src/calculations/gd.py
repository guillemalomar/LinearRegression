import logging
import numpy as np
import random

from src.settings import step_size, max_iterations, max_error
from src.messages import MESSAGES


def gradient_descent(input_data):
    thetas = initialize_thetas(input_data[0])
    logging.info(MESSAGES["Initial_thetas"].format(thetas))
    samples = len(input_data)
    iterations = 0
    c_error = 0.1
    new_thetas = []
    while iterations < max_iterations and max_error < c_error:
        for _ in range(0, len(input_data[0])):
            new_thetas.append(0)
        for ind, training_example in enumerate(input_data):
            cost = obtain_cost(training_example, thetas)
            new_thetas = obtain_new_thetas(new_thetas, cost, training_example, samples)
        new_thetas, c_error = update_thetas(new_thetas, thetas)
        thetas = list(new_thetas)
        new_thetas = []
        iterations += 1
    logging.info(MESSAGES["Iterations"].format(iterations))
    logging.info(MESSAGES["Final_thetas"].format(thetas))
    return thetas


def initialize_thetas(input_example):
    thetas = []
    for i in range(0, len(input_example)):
        thetas.append(random.randint(0, 5))
    thetas = np.array(thetas)
    return thetas


def update_thetas(new_thetas, thetas):
    updated_thetas = []
    total_error = 0
    for ind, theta in enumerate(thetas):
        error = step_size * new_thetas[ind]
        total_error += error
        updated_thetas.append(theta - error)
    updated_thetas = np.array(updated_thetas)
    return updated_thetas, abs(total_error)


def obtain_new_thetas(new_thetas, cost, training_example, samples):
    for ind, x in enumerate(training_example):
        if ind == 0:
            new_thetas[ind] += 1 / 2 * samples * cost
        else:
            new_thetas[ind] += 1 / 2 * samples * cost * training_example[0]
    return new_thetas


def obtain_cost(training_example, thetas):
    hypothesis = obtain_hypothesis(training_example, thetas)
    return hypothesis - training_example[-1]


def obtain_hypothesis(training_example, thetas):
    total = 0
    for ind, theta in enumerate(thetas):
        if not ind:
            total += theta
        else:
            total += training_example[ind - 1] * theta
    return total


def obtain_output_from_input(desired_input, trained_model):
    result = desired_input
    total = trained_model[0]
    for ind, val in enumerate(desired_input):
        total += val * trained_model[ind + 1]
    result.append(total)
    return result


def obtain_random_input(input_data):
    input_value = []
    for _ in range(0, len(input_data)-1):
        input_value.append(random.uniform(1.0, 4.0))
    logging.info(MESSAGES["Values_analyze"].format(input_value))
    return input_value
