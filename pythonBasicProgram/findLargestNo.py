#Given a List to Find third largest no.
data = [1,3,5,8,6,58,35,2,95,102]
#Assume data[0] is third largest no.
third_largest = data[0]
first_largest=int()
second_largest=int()
#Iterate first loop to get largest no.
for num1 in data:
    if num1 > third_largest:
        first_largest = num1
 #Iterate second loop to get second largest no.      
for num2 in data:
    
    if num2 is first_largest:
            continue
    if num2 > third_largest:
              second_largest= num2        
#Iterate third loop to get third largest no.
for num3 in data:
    if num3 == first_largest or num3 == second_largest:
        continue
    if num3 > third_largest:
        third_largest = num3
print(third_largest)               