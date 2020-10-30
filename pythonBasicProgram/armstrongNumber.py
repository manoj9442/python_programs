# Take input from user to check armstrong no
num = int(input(" Enter any no.to check armstrong : "))
temp = num
orig_num = num
count=0
sum = 0
#find no. of digits in number
while num >0:
    num = num //10
    count += 1
    #calculate to check armstrong no.
while temp > 0 :
    digit = temp % 10
    sum = sum + (digit**count)
    temp = temp // 10
    #check given no is an armstrong or not
if sum == orig_num:
    print(f"{orig_num} is an armstrong no. ")
else:
    print(f"{orig_num} is not an armstrong no.")        
     
