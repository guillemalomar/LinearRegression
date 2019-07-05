import argparse


def args_handler(argv):

    p = argparse.ArgumentParser(
        description='Linear Regression',
        formatter_class=argparse.RawTextHelpFormatter
    )

    p.add_argument('-f', '--file', action='store', type=str, default=None,
                   help='CSV input file. If not specified it will use a default one.')

    p.add_argument('-m', '--mode', action='store', type=str, default='GD',
                   help='Application mode: GD (Gradient Descent)| NM (Normal Equation). Default: GD')

    p.add_argument('-i', '--input', action='store', type=str, default=None,
                   help='Input values to process. Between \'s. Example: \'2.2 3.3\'. Default: Random')

    return p.parse_args(argv[1:])
