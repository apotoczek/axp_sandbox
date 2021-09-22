f1 = open('fixtures/a.csv', 'r')
f2 = open('fixtures/b.csv', 'r')
line = 0

print('Differences Found')

while True:
    lineF1 = f1.readline().strip()
    lineF2 = f2.readline().strip()
    line += 1

    if lineF1 or lineF2:
        if lineF1 != lineF2:
            print("Line %d (%s vs %s)" % (line, lineF1, lineF2))
    else:
        f1.close()
        f2.close()
        break
