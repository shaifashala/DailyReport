/*Python Program to remove duplicate elements from a list
 Description:
input[1,2,3,3,4,5,5,6]
Output[1,2,3,4,5,6]*/
a=[]
n= int(input("Enter the number of elements in list:"))
for x in range(0,n):
    element=int(input("Enter element" + str(x+1) + ":"))
    a.append(element)
b = set()
unique = []
for x in a:
    if x not in b:
        unique.append(x)
        b.add(x)
print("Non-duplicate items:")
print(unique)
