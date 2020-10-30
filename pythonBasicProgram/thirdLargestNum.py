#Given a List to Find third largest no.
data = [1,3,5,8,6,58,35,2,95,102]
#Assume this.
third_largest = int()
first_largest=data[0]
second_largest=data[1]
#compare first largest and second largest
if first_largest < second_largest:
    temp = first_largest
    first_largest = second_largest
    second_largest = temp
#Iterate  loop to get third largest no.
for i in range(2,len(data)):
    if data[i] > second_largest and data[i] > first_largest:
        third_largest =second_largest
        second_largest = first_largest
        first_largest = data[i]

    elif data[i] > second_largest:
        third_largest = second_largest
        second_largest = data[i]
print(third_largest)        
              