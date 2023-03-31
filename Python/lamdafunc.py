numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

filtered_numbers = list(map(lambda x: x * 2, filter(lambda x: x % 2 != 0, numbers)))

print(filtered_numbers)
