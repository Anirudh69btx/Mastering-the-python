#Write a function to remove characters from a string starting from index 0 up to n and return a new string.
def st(stri:str):  #   function kai parameter ko phele se define karne kai liye syntax:-(parameter:data_type)

    
    n=int(input("give index till you want to remove="))
    for i in stri[n+1: ]:
        print(i)
st("Anirudh") 