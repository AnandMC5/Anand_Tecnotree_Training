while True:
    try:
        a=input("Enter the filename: ")
        if a=="example.txt":
            with open(a) as file_object:
                 contents = file_object.read()
                 print(contents)
                 break
       



    except FileNotFoundError:
        print("Please enter the correct file name")