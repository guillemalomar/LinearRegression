import argparse
import csv
import logging
import numpy as np
import sys

from src.calculations.gd import gradient_descent
from src.calculations.ne import normal_equation
from src.calculations.gd import obtain_output_from_input
from src.calculations.gd import obtain_random_input
from src.tools.plot_tools import plot_points
from src.messages import MESSAGES
from src.settings import default_input_file

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s",
    handlers=[
        # logging.FileHandler("{0}/{1}.log".format("src", "execution")),
        logging.FileHandler("{}.log".format("execution")),
        logging.StreamHandler()
    ])


def args_handler(argv):

    p = argparse.ArgumentParser(
        description='Gradient Descent',
        formatter_class=argparse.RawTextHelpFormatter
    )

    p.add_argument('-f', '--file', action='store', type=str, default=None,
                   help='CSV input file. If not specified it will use a default one.')

    p.add_argument('-m', '--mode', action='store', type=str, default=None,
                   help='Application mode: GD (Gradient Descent)| NM (Normal Equation). Default: GD')

    p.add_argument('-i', '--input', action='store', type=str, default=None,
                   help='Input values to process. Between \'s. Example: \'2.2 3.3\'. Default: Random')

    return p.parse_args(argv[1:])


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
            matrix_y.append([z[-1]])
    matrix_x = np.array([np.array(xi) for xi in matrix_x])
    matrix_y = np.array([np.array(xi) for xi in matrix_y])
    return matrix_x, matrix_y


def _main(argv):
    args = args_handler(argv)

    logging.info(MESSAGES['Application_started'])

    if args.file:
        try:
            f = open(args.file, 'r')
            f.close()
        except FileNotFoundError:
            logging.error(MESSAGES["File_not_found"])
            sys.exit()
        title = args.file
    else:
        title = default_input_file

    if args.mode:
        mode = args.mode
        if mode not in ['GD', 'NE']:
            logging.error(MESSAGES["Wrong_mode"])
            sys.exit()
    else:
        mode = 'GD'

    mode = 'NE'
    if mode == 'GD':
        input_data = obtain_gd_input(title)
        result = gradient_descent(input_data)
    else:
        input_data, matrix_y = obtain_ne_input(title)
        result = normal_equation(input_data, matrix_y)

    if args.input:
        try:
            input_value = [float(x) for x in args.input.split(' ')]
            if len(input_value) != len(input_data[0]) - 1:
                raise ValueError
        except ValueError:
            logging.error(MESSAGES["Wrong_input"])
            sys.exit()
    else:
        input_value = obtain_random_input(input_data[0])

    calculated_value = obtain_output_from_input(input_value, result)
    logging.info(MESSAGES["Input_result"].format(calculated_value))
    plot_points(title, input_data, result, calculated_value)


if __name__ == '__main__':
    _main(sys.argv)
