#Variable Swapping
#Write a program to swap the values of two variables, a and b, without using a third temporary variable.
a = 5
b = 10
print(f"Before Swap: a = {a}, b = {b}")
a, b = b, a
print(f"After Swap: a = {a}, b = {b}")


#string swap -> string is immutable can't be swapped easily
text = "hello"
lst = list(text)
lst[2], lst[4] = lst[4], lst[2]
text = "".join(lst)
print(text)