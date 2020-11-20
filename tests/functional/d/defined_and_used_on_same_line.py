"""Check for definitions and usage happening on the same line."""
# pylint: disable=missing-docstring,multiple-statements,no-absolute-import,parameter-unpacking,wrong-import-position,unnecessary-comprehension
from __future__ import print_function
import sys
print([index for index in range(10)])

print((index for index in range(10)))


def FILTER_FUNC(x):
    return not x


def func(xxx):
    return xxx


def func2(xxx):
    return xxx + func2(1)


print(sys.exc_info())

for i in range(10):
    print(i)

j = 4


def LAMB(x):
    return x + j


def FUNC4(a, b):
    return a != b


# test http://www.logilab.org/ticket/6954:

with open('f') as f:
    print(f.read())

with open('f') as f, open(f.read()) as g:
    print(g.read())
