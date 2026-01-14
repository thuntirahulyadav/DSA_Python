#Find the Union and Intersection of the two sorted arrays.
def find_union(a,b):
    i=j=0
    union=[]
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
           if not union or union[-1] != a[i]:
              union.append(a[i])
           i += 1
        elif a[i] > b[j]:
             if not union or union[-1] != b[j]:
               union.append(b[j])
             j += 1
        else:
             if not union or union[-1] != a[i]:
               union.append(a[i])
             i += 1
             j += 1

    return union
def find_intersection(a,b):
     i=j=0
     intersection=[]
     while i < len(a) and j < len(b):
         if a[i] < b[j]:
            i += 1
         elif a[i] > b[j]: 
            j += 1
         else:
            intersection.append(a[i])
            i += 1
            j += 1
     return  intersection

n=int(input("enter the number of elements in array 1: "))
a=[]
for i in range(n):
    element=int(input("enter element:"))
    a.append(element)
    
m=int(input("enter the number of elements in array 2:"))
b=[]
for i in range(m):
    element=int(input("enter element:"))
    b.append(element)
print("the original array 1 is:",a)
print("the original array 2 is:",b)   
print(find_union(a,b)) 
print(find_intersection(a,b))
          