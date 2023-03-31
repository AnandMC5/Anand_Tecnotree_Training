l=[]
for i in range(5):
    a=int(input(f"Enter  number {i+1}: "))
    l.append(a)
print(f"After adding the elements the list is: {l}")
l.sort()
print(f"The maximum number in the list is:{l[-1]}\nThe minimum number in the list is:{l[0]}")