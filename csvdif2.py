import time


def main(f1, f2, outfile):
    with open(f1, 'r') as csv1, open(f2, 'r') as csv2:
        lines1 = csv1.readlines()
        lines2 = csv2.readlines()

    with open(outfile, 'w') as outFile:
        for line in lines2:
            if line not in lines1:
                outFile.write(line)


if __name__ == '__main__':
    input1 = input('CSV 1: ')
    input2 = input('CSV 2: ')
    default_outfile = 'csvdif2_' + str(int(time.time())) + '.txt'
    main(input1, input2, outfile=default_outfile)
