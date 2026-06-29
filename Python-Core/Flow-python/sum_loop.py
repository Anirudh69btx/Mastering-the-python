#Write a program that accepts a number from the user and calculates the sum of all numbers from 1 up to that number.
N=int(input("enter the value of Number till where we have to sum="))
sum=0
for i in range(0,N+1):
    sum+=i
print(sum)
