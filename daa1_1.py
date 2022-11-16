def fibonacci(n):
    if(n<=1):
        return n
    else:
        return (fibonacci(n-1)+fibonacci(n-2))
n=int(input("Enter the terms"))
if(n<0):
    print("Enter the correct value")
else:
    for i in range(n):
        print(fibonacci(i))
        
        
    