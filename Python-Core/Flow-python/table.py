# Create a program that takes an integer and prints its multiplication table from 2 to 10.
for i in range(2,51):
    for j in range(1,11):
        print(f"{i}*{j}={i*j}")
        if j==10:
            print("-------------------")