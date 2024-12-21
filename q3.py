#for given integer x, print true if its positive, print false if it is negative and print 0 if it is 0 

integer=int(input("Enter an integer="))
if integer<0:
    print("Integer is negative.")
elif integer==0:
    print("Integer is Zero.")
else:
    print("Integer is positive")