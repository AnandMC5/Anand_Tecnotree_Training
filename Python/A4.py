# l=[]
# a=int(input("Enter the number of elements you want to add to the list: "))
# for i in range(a):
#     j=int(input(f"Enter the element {i+1}: "))
#     l.append(j)
#     print(l)
# median=0
# sum=0
# for j in l:
#     sum+=j

# median=sum/len(l)
# print(median)


l=[]
a=int(input("Enter the number of elements you want to add to the list: "))
for i in range(a):
    j=int(input(f"Enter the element {i+1}: "))
    l.append(j)
    print(l)

if len(l)%2==0:
    sum=0
    for j in l:
        sum+=j
        median=0
        median=sum/len(l)
    print(median)

else:
    median=((len(l))/2)+1
    print(l[median])
