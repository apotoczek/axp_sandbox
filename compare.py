import sys
import getopt
import uuid
import time


def gen_files(n, c):
    print('Generating files with ' + str(n) + ' strings, ' + str(c) + ' in common:')

    foo_name = 'foo_' + str(int(time.time())) + '.txt'
    print(foo_name)

    bar_name = 'bar_' + str(int(time.time())) + '.txt'
    print(bar_name)

    foo = []
    bar = []
    if 0 < c <= n:
        for i in range(0, n, 1):
            foo.append(uuid.uuid4().hex)
        bar = foo[:c]
        for i in range(0, n - c, 1):
            bar.append(uuid.uuid4().hex)
    else:
        for i in range(0, n, 1):
            foo.append(uuid.uuid4().hex)
            bar.append(uuid.uuid4().hex)

    with open(foo_name, 'w') as f:
        for s in foo:
            f.write("%s\n" % s)

    with open(bar_name, 'w') as f:
        for s in bar:
            f.write("%s\n" % s)


def compare(foo_name, bar_name):
    print('Processing ' + foo_name + '...')
    foo = [line.rstrip('\n') for line in open(foo_name)]
    print('Processing ' + bar_name + '...')
    bar = [line.rstrip('\n') for line in open(bar_name)]

    sfoo = set(foo)
    sbar = set(bar)
    delta_foo = sfoo.difference(sbar)
    delta_bar = sbar.difference(sfoo)

    length = 0
    if len(sfoo) > len(sbar):
        length = len(sfoo)
    else:
        length = len(sbar)

    slength = 0
    if len(delta_foo) > len(delta_bar):
        slength = len(delta_foo)
    else:
        slength = len(delta_bar)

    common = length - slength
    print('There are ' + str(common) + ' strings in common between the files')


def main(argv):
    n = 0
    c = 0
    try:
        opts, args = getopt.getopt(argv, 'hn:c:', ['nstrings=', 'common='])
    except getopt.GetoptError:
        print('compare.py -n <gen files with n strings gte 1 lte 1M> -c <number of common strings between files>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('compare.py -n <gen files with n strings gte 1 lte 1M> -c <number of common strings between files>')
            sys.exit()
        elif opt in ("-n", "--nstrings"):
            n = int(arg)
        elif opt in ("-c", "--common"):
            c = int(arg)

    if 1 <= n <= 1000000 and 0 <= c <= 1000000:
        gen_files(n, c)
    elif n == 0:
        foo_name = input('File foo: ')
        bar_name = input('File bar: ')
        compare(foo_name, bar_name)
    else:
        print('compare.py -n <gen files with n strings gte 1 lte 1M> -c <number of common strings between files>')
        sys.exit(2)


if __name__ == "__main__":
    main(sys.argv[1:])
