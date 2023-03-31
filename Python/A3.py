l=[]
for i in range(6):
    a=input(f"Enter the string {i+1}: ")
    l.append(a)
print(f"list contains {l}")
l.sort()
print("\nStrings in alphabetical order:\n")
for i in l:
    print(i)