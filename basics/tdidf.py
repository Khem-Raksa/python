import math

x = int(input("Enter frequency: "))
N = int(input("Enter total documents: "))
n = int(input("Enter number of documents term appears in: "))

answer = (1 + math.log2(x)) * (math.log2(N/n))
print(answer)