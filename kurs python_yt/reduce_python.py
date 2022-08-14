lis = [1, 3, 5, 6, 2]
import functools
import itertools
import operator

print("The sum of the list elements is : ", end="")
print(functools.reduce(operator.add, lis))
print("The product of list elements is : ", end="")
print(functools.reduce(operator.mul, lis))
print("The summation of list using accumulate is :", end="")
print(list(itertools.accumulate(lis, lambda x, y: x + y)))
