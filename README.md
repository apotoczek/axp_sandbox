# Assessment

1. [Distinct Numbers](#1-distinct-numbers)
2. [Strings Comparison](#2-strings-comparison)

## 1. Distinct Numbers

#### Question:

> The generator starts by returning the value at index 0. ​It then uses that value as the index for the next value to return, and so on​. If the generator was seeded with the list [1, 2, 0], the first number it would return would be 1, then 2, then 0, and then it would repeat the sequence. Thus, the number of distinct values would be 3."

#### Part a:

> Write a function that takes as input the seed list of the random number generator of up to 1 million integers and returns the count of distinct integers the random number generator would return.

#### Solution:

Python script `distinct.py`, executable from CLI, e.g.: `python distinct.py -n 10 -d False`

Args:

`-n, --nlength` length of the random integer seed list, 1 < n <= 1M

`-d, --distinct` True or False, generate seed list of distinct or non-distinct ints

#### Examples:

```
$ python distinct.py -n 10 -d True
Distinct seed list:
[2, 9, 8, 4, 5, 6, 0, 1, 7, 3]
Distinct values found using algorithm and their count:
[2, 8, 7, 1, 9, 3, 4, 5, 6, 0] 10
```

```
$ python distinct.py -n 10 -d False
Non-distinct seed list:
[3, 9, 5, 6, 8, 7, 1, 6, 9, 3]
Distinct values found using algorithm and their count:
[3, 6, 1, 9] 4
```

> Note: per requirements, the final count number (10, or 4 in examples) stops checking for further distinct ints once a dupe is found; the bottom list printed shows the ints counted.

> Note: script developed with Python 3.8.2 using virtualenv, but works in 2.7, 3.4, 3.6

#### Implementation:

Script executes the seed generator `random_num(n, distinct)` and passes the seed list to the algorithm in `distinct_num(ran_list)`, which traverses the seed list and saves each distinct value to a new list, for comparison to the next loop iteration, until a duplicate is found or the whole list has been checked.  The new list length then represents the count of distinct values in the seed list, according to the algorithm defined in the requirements.  Once a duplicate is found, no further distinct ints are counted.

#### Part b:

> Can part a be done with O(1) auxiliary space (i.e. using only a constant amount of additional memory)? If so, write a function that does it. If not, why not?

#### Answer:

The algorithm takes a seed list of arbitrary length based on user input, so it cannot be assigned a Constant complexity.  It is O(n), Linear complexity based on the length of the seed list iterated through in a loop. 


## 2. Strings Comparison

#### Question:

asdf

#### Part a:

jkl

#### Part b:

foo