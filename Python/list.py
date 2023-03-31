# //Demo examples:List comprehension

# // Eg:1
# create a new list of squares of numbers from 1 to 10
# squares = [i**3 for i in range(0, 12)]
# print(squares) 


# //Eg:2
# create a new list of even numbers from an existing list
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# evens = [i for i in numbers if i / 2 == 0]
# print(evens)



# create a new list of strings, where each string is the original string capitalized
words = ['APPLE', 'BANANA', 'CHERRY', 'DATE']
capitalized = [word.capitalize() for word in words]
print(capitalized) 

