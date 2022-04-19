import time
from tracemalloc import start
def calcProd():
       # Calculate the product of the first 100,000 numbers.
       product = 1
       for i in range(1, 100000):
           product = product * i
       return product

startTime = time.time()
prod = calcProd()
endTime = time.time() 

print('Took %s seconds to calculate.'%(endTime-startTime))
