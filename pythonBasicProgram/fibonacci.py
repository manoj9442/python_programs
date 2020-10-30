#Take input from user to print fibonacci series upto nterms
nterms = int(input("Enter nth terms... : "))
n1 = 0
n2 = 1
if nterms < 0:
    print("Please Enter a Positive Number")
elif nterms ==1:
    print(f"Fibonacci series of {nterm} is 1.")
else:
    for i in range(nterms):
        print(n1)
        temp=n1+n2
        n1 = n2
        n2 = temp    