import csv


def obtain_input(input_file):
    with open(input_file) as csvfile:
        file = csv.reader(csvfile, delimiter="\t")
        matrix = []
        for ind, z in enumerate(file):
            if ind == 0:
                continue
            z[:5] = map(float, z[0:5])
            matrix.append(z)
    return matrix
