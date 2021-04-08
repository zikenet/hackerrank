#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())
    LIST_VALUES = []

    for N_itr in range(N):
        firstNameEmailID = input().split()
        firstName = firstNameEmailID[0]
        emailID = firstNameEmailID[1]

        if emailID.endswith("@gmail.com"):
            LIST_VALUES.append(firstName)

    LIST_VALUES.sort()
    for val in LIST_VALUES:
        print(val)
