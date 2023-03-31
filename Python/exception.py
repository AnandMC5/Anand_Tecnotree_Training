while True:
    try:
       a=int(input("Enter a number 1: "))
       b=int(input("Enter a number 2: "))
       r=a/b
       print(r)
       break
    except ZeroDivisionError:
        print("Zero division error: Please enter the denominator other than 0")



