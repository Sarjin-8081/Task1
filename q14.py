group=int(input("enter number of students in class A="))
group1=int(input("enter number of students in class B="))
group2=int(input("enter number of students in class C="))
if group<=20:
    desk=group/2
    print(f"Number of desk u need is {desk} for section A")
elif group1>group:
    desk=group1/2
    print(f"Number of desk u need is {desk} for section B")
elif group2>group1:
    desk=group2/2
    print(f"Number of desk u need is {desk} for section C")