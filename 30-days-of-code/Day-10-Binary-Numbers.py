
#!/bin/python

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    
    N = int(input())
    DATA = bin(N)
    
    MAXIMUM = 0
    CURRENT = 0
    
    for num in DATA:
        
        if num == '1':
            CURRENT = CURRENT + 1
        
        else:
            MAXIMUM = max(MAXIMUM, CURRENT)
            CURRENT = 0

print(max(MAXIMUM, CURRENT))