import argparse
import logging
import sys

from src.calculations.calculations import gradient_descent
from src.calculations.calculations import obtain_output_from_input
from src.calculations.calculations import obtain_random_input
from src.tools.plot_tools import plot_points
from src.tools.file_tools import obtain_input


def args_handler(argv):

    p = argparse.ArgumentParser(
        description='Gradient Descent',
        formatter_class=argparse.RawTextHelpFormatter
    )

    p.add_argument('-f', '--file', action='store', type=str, default=None,
                   help='CSV input file. If not specified it will generate it from the MYSQL data.')
    return p.parse_args(argv[1:])


def _main(argv):
    args = args_handler(argv)

    if args.file:
        try:
            f = open(args.file, 'r')
            f.close()
        except FileNotFoundError:
            logging.error("RIP")
            sys.exit()
        title = args.file
    else:
        title = '../input/2D.csv'

    input_data = obtain_input(title)
    input_value = obtain_random_input(input_data[0])
    result = gradient_descent(input_data)
    calculated_value = obtain_output_from_input(input_value, result)
    plot_points(title, input_data, result, calculated_value)


if __name__ == '__main__':
    _main(sys.argv)
