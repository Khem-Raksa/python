"""
Integration function : Scalar product + bias

x - input vector
w - weights to signify strengths
b - bias

"""

def integration (x,w,b):
    weighted_sum = sum(x[k] * w[k] for k in range(0,len(x)))
    return weighted_sum + b


#Not
# def wrong_integration (x,w,b):
#     weighted_sum = 0
#     for weight in w:
#         for input_element in x:
#             weighted_sum += weight * input_element
#     return weighted_sum + b
# This is wrong because it adds every multiplication pair and pair-wise. Basically, it is not scalar-product