#!/usr/bin/python

# import random
#
# res = random.sample(range(0, 7), 7)
#
# print("Random number list is : " + str(res))
#
# print(res[6])


# def isprime(n):
#	'''check if integer n is a prime'''
#
#	# make sure n is a positive integer
#	n = abs(int(n))
#
#	# 0 and 1 are not primes
#	if n < 2:
#		return False
#
#	# 2 is the only even prime number
#	if n == 2:
#		return True
#
#	# all other even numbers are not primes
##	if not n & 1:
##		return False
#
#	# range starts with 3 and only needs to go up
#	# the square root of n for all odd numbers
#	for x in range(3, int(n**0.5) + 1, 2):
#		if n % x == 0:
#			return False
#
#	return True
#
# print(isprime(11))


#
# try:
#	l = (1, 2, 3, 4)
# except Ex
# print(l.index(5))


# import random
# my_randoms = random.sample(xrange(0, 10), 10)
# print(my_randoms)


# import random
# my_randoms = [random.randrange(0,10,1) for _ in range(10)]
# print(my_randoms)


import uuid

foo = []
bar = []
for i in range(0, 10, 1):
    foo.append(uuid.uuid4().hex)
    bar.append(uuid.uuid4().hex)

# foo = [2, 9, 8, 4, 5, 6, 0, 1, 7, 3]
# bar = [2, 8, 7, 1, 9, 3, 4, 5, 0, 6]

# foo = [2, 9, 8, 4, 5, 6, 0, 1, 2, 2]
# bar = [2, 8, 7, 1, 9, 3, 4, 5, 0, 0]


sfoo = set(foo)
sbar = set(bar)

# print('sfoo: ' + str(sfoo))
# print('sbar: ' + str(sbar))

delta_foo = sfoo.difference(sbar)
# if not delta_foo:
#     print('foo - no difference: ' + str(delta_foo))
# else:
#     print('foo - difference: bar missing ' + str(delta_foo))

delta_bar = sbar.difference(sfoo)
# if not delta_bar:
#     print('bar - no difference: ' + str(delta_bar))
# else:
#     print('bar - difference: foo missing ' + str(delta_bar))

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

# print(
#	str(length) + ' - (' + str(len(delta_foo)) + ' + ' + str(len(delta_bar)) + ')'
#	)
print(
    str(length) + ' - ' + str(slength)
)

# import uuid
#
# l1 = []
# l2 = []
#
# for i in range(0, 10, 1):
#	l1.append(uuid.uuid4().hex)
#	l2.append(uuid.uuid4().hex)

# print(l1)
# print(l2)


