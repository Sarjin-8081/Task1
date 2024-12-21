cost=int(input("Enter cost price of bike in Rs="))
if cost>100000:
    tax=cost*15/100
    print(tax)
elif cost>50000 and cost<=100000:
    tax=cost*10/100
    print(tax)
elif cost<=50000:
    tax=cost*5/100
    print(tax)