""" Take both input from user(from where and upto) 
to print all prime no. in this interval"""

from_where = int(input("Enter From where... : "))
upto = int(input("Enter Upto... : "))
for num in range(from_where,(upto + 1)):

    if num > 1:

        for i in range(2,num):

            if (num % i) == 0:
                break
        else:
             print(num)    

    