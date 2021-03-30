
#Enter your code here. Read input from STDIN. Print output to STDOUT
from __future__ import print_function


N = int( raw_input() )

for i in range( 0, N ):

    string = raw_input()

    for j in range( 0, len(string) ):

        if j % 2 == 0:

            print(string[j], end="")

    print(" ", end="")

    for k in  range( 0, len(string) ):

        if k % 2 != 0:

            print(string[k], end="")

    print("") 


