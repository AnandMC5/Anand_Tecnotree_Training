def longestword(word_list):
    longest_word = ""
    for word in word_list:
        if len(word) > len(longest_word):
            longest_word = word
    print(f"The longest word in the list is : {longest_word}")

l=[]
a=int(input("Enter the number of elements you want to add to the list: "))
for i in range(a):
    e=input(f"Enter the word {i+1}: ")
    l.append(e)

longestword(l)

