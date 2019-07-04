from src.tools.file_tools import obtain_input
import random


def gradient_descent(input_file):
    input_data = obtain_input(input_file)
    step_size = 0.01
    thetas = []
    for i in range(0, len(input_data[0])):
        thetas.append(random.randint(0, 5))
    print(thetas)
    samples = len(input_data)
    for i in range(0, 10000):
        new_thetas = []
        for _ in range(0, len(input_data[0])):
            new_thetas.append(0)
        for ind, training_example in enumerate(input_data):
            cost = obtain_cost(training_example, thetas)
            new_thetas = obtain_new_thetas(new_thetas, cost, training_example, samples)
        new_thetas = update_thetas(new_thetas, thetas, step_size)
        if check_converged(thetas, new_thetas):
            print(i)
            break
        thetas = new_thetas
    print(new_thetas)
    return input_data, new_thetas


def check_converged(thetas, prev_thetas):
    for ind, theta in enumerate(thetas):
        if not (theta - prev_thetas[ind]) ** 2 < 0.0000001:
            return False
    return True


def update_thetas(new_thetas, thetas, step_size):
    updated_thetas = []
    for ind, theta in enumerate(thetas):
        updated_thetas.append(theta - (step_size * new_thetas[ind]))
    return updated_thetas


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
