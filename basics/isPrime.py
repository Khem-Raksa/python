def isPrime(n):
    if n<=1:
        return False # 1 is not prime
    else:
        #note that the n (end) in range is exclusive
        #so we test n by dividing it by 2 until itself
        #we only need to test until n-1 since we know n divides n
        #and just need to divide dach once to make it not prime
        for i in range(2,n):
            if n%i==0:
                return False
        return True

#Test
print(isPrime(1))
print(isPrime(2))
print(isPrime(3))
print(isPrime(17))