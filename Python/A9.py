l=[]
a=int(input("Enter the number of elements you want to add to the list: "))
for i in range(a):
    j=int(input(f"Enter the element {i+1}: "))
    l.append(j)
    print(f"old list: {l}")
j=[]
for p in l:
    r=p*p
    j.append(r)
print(f"new list: {j}")