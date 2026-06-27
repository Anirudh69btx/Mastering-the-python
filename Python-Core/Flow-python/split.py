#Write a program that takes three names (or any words) from a user in a single input prompt and assigns them to three separate variables.
a,b,c=str(input("enter the name =")).split()
print(f"first_name={a}\nMiddle_name={b}\nLast_name={c}")