def str_uplow():

    str= input("Enter a string :")

    print("Entered string is :",str)

    str_upper=0
    str_lower=0

    for i in str:
    
        if i.isupper():
            str_upper+=1
        elif i.islower():
            str_lower+=1
    return str_upper,str_lower

data = str_uplow()
print("No. of Uppercase letters, No. of  Lowercase letters:",data)
