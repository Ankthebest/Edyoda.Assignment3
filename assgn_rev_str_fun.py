def rev_str():
    str = input("Enter a string for ex. '1234abcd': ")
      
    print("The original string is:",str) 
    
    rev = "" 
    for i in str:  
        rev = i + rev 
    return rev

reversed = rev_str()

print("The reverse  string is:",reversed)