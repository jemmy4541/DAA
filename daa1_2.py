n=int(input("Enter the terms you want to entered"))
n1,n2=0,1
count=0
if(n<1):
    print("Invaldi")
elif(n==1):
    print(n1)
else:
    while(count<n):
        print(n1)
        temp=n1+n2
        n1=n2
        n2=temp
        count+=1
