import sys
import getopt
import random


def random_num(n, distinct):
    print('\n')
    if distinct:
        print('Distinct seed list:')
        my_randoms = random.sample(range(0, n), n)
    else:
        print('Non-distinct seed list:')
        my_randoms = [random.randrange(0, n, 1) for _ in range(n)]

    print(my_randoms)
    print('\n')
    return my_randoms


def distinct_num(ran_list):
    unq_list = []
    j = 0
    for i in range(len(ran_list)):
        if i > 0 and j != 0 or i == 0:
            if ran_list[j] in unq_list:
                break
            unq_list.append(ran_list[j])
        j = ran_list[j]

    print('Distinct values found using algorithm and their count:')
    print(str(unq_list) + " " + str(len(unq_list)))
    print('\n')


def main(argv):
    n = 0
    d = False
    try:
        opts, args = getopt.getopt(argv, 'hn:d:', ['nlength=', 'distinct='])
    except getopt.GetoptError:
        print('distinct.py -n <seed list length gt 1 lte 1M> -d <seed with distinct ints default False>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('distinct.py -n <seed list length gt 1 lte 1M> -d <seed with distinct ints True or False>')
            sys.exit()
        elif opt in ("-n", "--nlength"):
            n = int(arg)
        elif opt in ("-d", "--distinct"):
            d = (arg.lower() == 'true')

    if 1 < n <= 1000000:
        distinct_num(random_num(n, d))
    else:
        print('distinct.py -n <seed list length gt 1 lte 1M> -d <seed with distinct ints True or False>')
        sys.exit(2)


if __name__ == "__main__":
    main(sys.argv[1:])
