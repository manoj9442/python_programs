#Take input  to check palindrome
string = input("Enter Something... : ")
#set count to zero
is_palindrome = True
#Length of string 
len_of_string = len(string)
# iterate for loop upto half of given  string length
for i in range(len_of_string // 2):
    #compare corresponding element
    if string[i] is not string[len_of_string-i-1]:
        is_palindrome =False
        break
    else:
        is_palindrome = True

if is_palindrome:
    print(f"{string} is a palindrome.")
else:
    print(f"{string} is not a palindrome.")                
    