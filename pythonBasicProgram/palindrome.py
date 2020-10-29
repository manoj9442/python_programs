#Take input  to check palindrome
string = input("Enter Something... : ")
#set count to zero
count = 0
#Length of string 
len_of_string = len(string)
# iterate for loop upto half of given  string length
for i in range(len_of_string // 2):
    #compare corresponding element
    if string[i] is string[len_of_string-i-1]:
        count += 1
    else:
        count = 0

if count > 0:
    print(f"{string} is a palindrome.")
else:
    print(f"{string} is not a palindrome.")                
    