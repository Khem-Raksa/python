 # 1 method
    # table = list(itertools.product([1, 0], repeat=n))
    # for row in table:
    #     print(row)

import itertools
import numpy as np

def truth_table(n):
    cols = n
    rows = 2**n
    table = [[0 for x in range(rows)] for y in range(cols)]

    temp = (2**n)//2
    for row in range (0,n): # go into row 1 1
        # while(temp>0):
        for i in range (0,temp):
                table[row//2][i] = 1
                temp = temp//2
    table = np.transpose(table)

    for row in table:
        print(row)

n = int(input("Enter a number: "))
truth_table(n)


