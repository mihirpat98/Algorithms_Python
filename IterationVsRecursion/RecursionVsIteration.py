# Iteration
def factorial_i(number):
    product = 1
    for i in range(number):
        product *= (i+1)
    return product

# Recursion

def factorial_r(number):
    if number<=1: # base case
        return 1
    else:
        return number*factorial_r(number-1)