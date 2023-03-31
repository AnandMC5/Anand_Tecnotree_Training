l=[]
for i in range(5):
    a=int(input(f"Enter the number {i}: "))
    l.append(a)
print(f"The numbers in the list is:{l}")
sum=0
for j in l:
    if(j%2==0):
        sum+=j
print(sum)

