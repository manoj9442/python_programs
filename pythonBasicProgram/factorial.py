#Take input from user to get their factorial
num = int(input("Enter any number to get Factorial... : "))
pre_num = num
fact=1
#Check given number should not be negztive
if num < 0:
    print(" Please Enter Positive No. ")
if num is 1:
    print(f" Factorial of 1 is 1.")
else:
    while num > 0:
        fact = fact * num 
        num = num-1
print(f" Factorial of {pre_num} is {fact} .")           