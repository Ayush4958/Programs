num = int(input("Enter your Number :- "))
prime = (num , " is a prime number")
composite = (num , " is a composite number")
count = 0

for i in range(2,num):
    if(num%i==0):
        count = count + 1
        if(count<1):
            print(prime) 
            break
        else:
            print(composite)
