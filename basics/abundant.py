"""
Write a Python program to find out, if the given number is abundant. 
Note: In number theory, an abundant number or excessive number is a number for which the sum of its proper divisors is greater than the number itself.
 The integer 12 is the first abundant number. Its proper divisors are 1, 2, 3, 4 and 6 for a total of 16.
Test Data:
If is_abundant(12)
If is_abundant(13)
Expected Output:
True
False
"""

def isAbundant (n):
    lst = []
    for i in range (1,n):
        if n%i == 0:
            lst.append(i)
    if sum(lst) > n:
        return True
    else:
        return False

#Test
n = int(input("Please input an interger: "))
print(isAbundant(n))
