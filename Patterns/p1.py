n=4
#Left Traingle
for i in range (n):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")   
    print()     
for i in range (n):
    for j in range(i):
        print(" ",end=" ")
    for j in range(n-i):
        print("*",end=" ")   
    print()  

#Right Traingle
for i in range(n):
    for j in range(i):
        print("*",end=' ')    
    print()
for i in range(n):
    for j in range(n-i):
        print("*",end=' ')    
    print()

#Pyramid
for i in range(n):
    print(" "*(n-i-1),end='')
    for j in range(i+1):
        print("* ",end='')
    print()  
for i in range(n):
    print(" "*(i),end="")
    for j in range(n-i-1):
        print(" *",end='')
    print()          

    