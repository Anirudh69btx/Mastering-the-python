#Intermediate Level (15 Questions)
#Write a function that returns the greatest among three numbers.
def greate_r(a,b,c):
    largest=a
    if largest<b:
        largest=b
    if largest<c:
        largest=c
    print(largest)
greate_r(10,20,50)

def grea_ter(a,b,c):
    return max(a,b,c)
grea_ter(10,20,60)

def greater(a,b,c):
    if(a>b and a>c):
        print(f"{a} is greater than {b} and {c}")
    elif(b>c and b>a):
        print(f"{b} is greater than {a}and {c}")
    else:
        print(f"{c} is greater than {a} and {b}")
greater(10,50,5)
#Write a function that returns the absolute value of a number without using abs().
#using abs()
def absolute_value(a):
    return abs(a)

print(absolute_value(-5))
print(absolute_value(10))
#without using it 
def absolute(a):
    if(a<0):
        a=a*(-1)
    return

Write a function that checks whether a number is divisible by both 3 and 5.
def div(a):
    if(a%3==0 and a%5==0):
        print( f("{a} is divisble by both 3 and 5"))
    else:
        print( f"{a} is not divisble by either 3 or 5 or both")
div(115)
Write a function that returns the factorial of a number.
def fac(a):
    if a < 0:
        return "Factorial is not defined for negative numbers"

    if a == 0:
        return 1
    mul=a
    while a!=1:
        a=a-1
        mul=mul*a
    return mul
print(fac(3))
Write a function that counts how many even numbers exist from 1 to n.
def coun(n):
    count=0
    for i in range(1,n):
        if i%2==0:
            count+=1
    return count()
print(coun(5))
Write a function that reverses an integer.

Write a function that checks whether a number is a palindrome.
Write a function that returns the sum of digits of an integer.
Write a function that returns the largest digit in a number.
Write a function that checks whether a number is prime.
Write a function that returns the nth Fibonacci number.
Write a function that finds the GCD of two numbers.
Write a function that determines whether two strings are anagrams.
Write a function that counts vowels in a string.
Write a function that returns the second largest number in a list.