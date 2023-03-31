#intializing the empty dictionary
l=[]
a=int(input("Enter the number of elements you want to add to the list: "))
for i in range(a):
    j=input(f"Enter the String {i+1}: ")
    l.append(j)
print(l)

#intializing the empty dictionary
j=[]
for p in l:
    if p==p[::-1]:
        j.append(p)
print(f"The List containing only palindrome strings: {j}")
        