import math
import os
import random
import re
import sys


def check_weird(num):
    if num % 2 == 1:  # odd
        print("Weird")
    else:  # even
        range_2_5 = range(2, 5)
        range_6_20 = range(6, 21)
        range_20_100 = range(21, 101)
        if num in range_2_5:
            print("Not Weird")
        elif num in range_6_20:
            print("Weird")
        elif num in range_20_100:
            print("Not Weird")


if __name__ == '__main__':
    n = int(input().strip())
    check_weird(n)