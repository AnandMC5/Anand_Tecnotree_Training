def lettercount(s):
    l_count = {}
    for char in s:
        if char in l_count:
            l_count[char] += 1
        else:
            l_count[char] = 1

    return l_count

s = "Hello Anand!"
result = lettercount(s)
print(result)


