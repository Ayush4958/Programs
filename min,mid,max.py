# Arranging the 3 number in increasing order according to their value

a = int(input("Enter your first number:-"))
b = int(input("Enter your second number:-"))
c = int(input("Enter your third number:-"))

min=mid=max=None    # taking Variable and gave them same value 

# using if-else for logic building

if a<b and a<c:
    if b<c:
        min,mid,max=a,b,c
    else:
        min,mid,max=a,c,b

elif b<a and b<c:
    if a<c:
        min,mid,max=b,a,c
    else:
        min,mid,max=b,c,a
            
else:
    if a<b:
        min,mid,max=c,a,b
    else:
        min,mid,max=c,b,a
            
print("The number will be print in increasing order",min,mid,max)