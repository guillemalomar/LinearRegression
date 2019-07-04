import argparse
import logging
import sys

from src.calculations.calculations import gradient_descent
from src.tools.plot_tools import plot_points


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
    input_data, result = gradient_descent(title)
    plot_points(title, input_data, result)


if __name__ == '__main__':
    _main(sys.argv)
