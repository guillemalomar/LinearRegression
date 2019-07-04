import argparse
import csv
import logging
import sys

from src.calculations.calculations import gradient_descent
from src.calculations.calculations import obtain_output_from_input
from src.calculations.calculations import obtain_random_input
from src.tools.plot_tools import plot_points
from src.messages import MESSAGES
from src.settings import default_input

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s",
    handlers=[
        logging.FileHandler("{0}/{1}.log".format("src", "execution")),
        logging.StreamHandler()
    ])


def args_handler(argv):

    p = argparse.ArgumentParser(
        description='Gradient Descent',
        formatter_class=argparse.RawTextHelpFormatter
    )

    p.add_argument('-f', '--file', action='store', type=str, default=None,
                   help='CSV input file. If not specified it will use a default one.')

    p.add_argument('-i', '--input', action='store', type=str, default=None,
                   help='Input values to process. Between \'s. Example: \'2.2 3.3\'')

    return p.parse_args(argv[1:])


def obtain_input(input_file):
    with open(input_file) as csv_file:
        file = csv.reader(csv_file, delimiter="\t")
        matrix = []
        for ind, z in enumerate(file):
            if ind == 0:
                continue
            z[:5] = map(float, z[0:5])
            matrix.append(z)
    return matrix


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
        title = default_input
    input_data = obtain_input(title)

    if args.input:
        try:
            input_value = [float(x) for x in args.input.split(' ')]
            if len(input_value) != len(input_data[0]) - 1:
                raise Exception
        except:
            logging.error(MESSAGES["Wrong_input"])
            sys.exit()
    else:
        input_value = obtain_random_input(input_data[0])

    result = gradient_descent(input_data)
    calculated_value = obtain_output_from_input(input_value, result)
    logging.info(MESSAGES["Input_result"].format(calculated_value))
    plot_points(title, input_data, result, calculated_value)


if __name__ == '__main__':
    _main(sys.argv)
