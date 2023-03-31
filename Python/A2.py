a=input("Enter the String: ")
s=''
for j in a:
    if(j=="a" or j=="e" or j=="i" or j=="o" or j=="u"):
        continue
    else:
        s+=j
print(s)