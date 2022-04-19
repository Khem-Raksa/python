u = {i for i in range(1,101)}
print(u)

A = {i for i in range(1,101) if i%3==0}
print(A)

B = {i for i in range(1,101) if i%5==0}
print(B)

print("******")

A_and_B = A.intersection(B)
print(A_and_B)

A_or_B = A.union(B)
print(A_or_B)

A_minus_B = A.difference(B)
print(A_minus_B)

print("******")

#Cardinals
print(len(A))

print(len(B))

print(len(A_and_B))

print(len(A_or_B))

print(len(A_minus_B))