#computes the cartesian product of input iterables.
# given a two lists  and . Your task is to compute their cartesian product
#The first line contains the space separated elements of list .
#The second line contains the space separated elements of list .
#Both lists have no duplicate integer elements.

from itertools import product


a = map(int, input().split())
b = map(int, input().split())

print(' '.join(map(str,list(product(a,b)))))