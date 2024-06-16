m=int(input("Enter the number: "))
flag=0
if m<0:
    flag=1
elif m==1:
    flag=0
else:
    for i in range(2,(m//2)+1):
        if(m%i==0):
            flag=0
            break
if(flag==1):
    print("invalid prime")
else:
    print("valid prime")
        