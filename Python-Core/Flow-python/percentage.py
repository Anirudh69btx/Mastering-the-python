#Ask the user for a numerator and a denominator. Calculate the percentage (numerator/denominator * 100) and display it with exactly two decimal places followed by a percent sign.
nume=float(input("enter the number="))
deno=float(input("enter the number="))
per=(nume/deno)*100
print('%.2f' %per)