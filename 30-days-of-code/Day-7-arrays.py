
#!/bin/python

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    
    n = int( raw_input() )

    arr = map( int, raw_input().rstrip().split() )

    arr.reverse()

    for i in range(0, n):

        print arr[ i ], 
