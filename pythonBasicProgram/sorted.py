#Given a List
data = [1,3,5,1,34,6,7,87,9,2,56,90]

def sorted(data):
    #Find length of Given List
    length_of_list = (len(data))
    #Iterate For loop for upto length of Given List
    for i in range(length_of_list):
        #Iterate second for loop
        for j in range(length_of_list - i - 1):
            #compare two consecutive element and swap
            if(data[j] > data[j+1]):
                temp = data[j]
                data[j] = data[j+1];
                data[j+1] = temp 

    return data        
     
sorteddata = sorted(data) 
print(sorteddata)   




    


