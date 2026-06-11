#Write a Python function that accepts two integer numbers. If the product of the two numbers is less than or equal to 1000, return their product; otherwise, return their sum.
def calculate(a,b):
    if(a*b<=1000):
        print(a*b)
    else:
        print(a+b)
calculate(1115,7)