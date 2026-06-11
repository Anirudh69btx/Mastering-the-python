#Write a Python function that accepts two integer numbers. If the product of the two numbers is less than or equal to 1000, return their product; otherwise, return their sum.
def calculate(a,b):
    if(a*b<=1000):
        print(a*b)
    else:
        print(a+b)
calculate(1115,7)
#Beginner Level (5 Questions)
#Write a function that accepts one number and returns its square.
def sqaure(a):
    print(a*a)
sqaure(5)
#Write a function that accepts two numbers and returns the larger number.
def larger(a,b):
    if(a>b):
        print(f"{a} is greater than {b}")
    else:
        print(f"{b} is greater than {a}")
larger(4,5)
#Write a function that returns "Even" if a number is even; otherwise, return "Odd".
def even_and_odd(a):
    if(a%2==0):
        print(f"The number is even {a}")
    else:
        print(f"The number is odd {a}")
even_and_odd(20)
#Write a function that returns "Positive", "Negative", or "Zero" depending on the input number.
def number(a):
    if(a==0):
        print(f"{a} is zero")
    elif(a>0):
        print(f"{a} is postive")
    elif(a<0):
        print(f"{a} is negative")
number(1)