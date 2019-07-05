import sys

from src.log_tools import *
from src.calculations.gd import gradient_descent
from src.calculations.ne import normal_equation
from src.calculations.gd import obtain_output_from_input
from src.calculations.gd import obtain_random_input
from src.tools.plot_tools import plot_points
from src.tools.input_tools import obtain_gd_input, obtain_ne_input
from src.messages import MESSAGES
from src.settings import default_input_file
from src.args import args_handler


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

    mode = args.mode
    if mode not in ['GD', 'NE']:
        logging.error(MESSAGES["Wrong_mode"])
        sys.exit()

    if mode == 'GD':
        input_data = obtain_gd_input(title)
        result = gradient_descent(input_data)
    else:
        input_data = obtain_gd_input(title)
        matrix_x, matrix_y = obtain_ne_input(title)
        result = normal_equation(matrix_x, matrix_y)

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
