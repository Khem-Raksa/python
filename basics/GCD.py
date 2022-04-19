# gcd = hcf = highest common factor

def gcd(a,b):
    if b == 0: return a
    return gcd(b, a%b)

def gcd_of_2_nums(first_num,second_num):
    if(first_num > second_num):
        a = first_num
        b = second_num
        r = first_num % second_num
        while(r >0):
            a = b
            b = r
            r = a % b 
        # when r in line above above is zero 
        # , then b the new first num is the answer (according to euclid algorithm)
        answer = b 
    
    elif(first_num < second_num):
        a = first_num 
        b = second_num
        r = second_num % first_num
        while(r > 0):
            b = a
            a = r
            r = b % a
        answer = a
    else:
        answer = first_num
    return answer

# print(gcd_of_2_nums(102,70))
# print(gcd_of_2_nums(70,102))

# print(gcd_of_2_nums(3,3))

# print(gcd_of_2_nums(252,189))
# print(gcd_of_2_nums(189,252))

# print(gcd_of_2_nums(1000,500))

# print(gcd_of_2_nums(17,16))

# print(-17 % 2)
# print(-101 % 13)
# print(144 % 7)
# print(199 % 19)

# print(-111/99)
# print(-111%99)

# print(-9999%101)

# print(gcd_of_2_nums(123,277))
# print(gcd_of_2_nums(1529, 14038))
# print(gcd_of_2_nums(1529, 14039))

print(gcd_of_2_nums(55,21))

print(gcd(55,21))
print(gcd(201,111))
print(gcd(6,3))
# print(529%41)