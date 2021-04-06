#!/bin/python

from __future__ import division
import math
import os
import random
import re
import sys

# Complete the solve function below

def solve(meal_cost, tip_precent, tax_percent):
    tip = meal_cost * ( tip_percent / 100 )
    tax = meal_cost * ( tax_percent / 100 )
    totalCost = round( meal_cost + tip + tax )

    print int( totalCost )


if __name__ == '__main__':
    meal_cost = float(raw_input())

    tip_percent = int(raw_input())

    tax_percent = int(raw_input())

    solve(meal_cost, tip_percent, tax_percent)
