while True:
        print("\n---------------------------Simple Calculator------------------------------\n")
        #for taking user input
        num1=float(input("Enter the Number 1: "))
        num2=float(input("Enter the Number 2: "))
        
        #mathematical Operation
        print("\n----------------------------------------------------------------------")
        print("Select The operation you want to perform:")
        print("1.Addition")
        print("2.Subtraction")
        print("3.Multiplication")
        print("4.Division")
        print("5.For Remainder")
        print("6.Exit")
        print("----------------------------------------------------------------------")

        choice=int(input("\nEnter the choice of operation you want to perform: "))
        #for Addition
        if choice==1:
                result=num1+num2
                print("----------------------------------------------------------------------")
                print(f"The addition of {num1} and {num2} is :{result} ")
                print("----------------------------------------------------------------------")
        #for Subtraction
        elif choice==2:
                result=num1-num2
                print("----------------------------------------------------------------------")
                print(f"The Subtraction of {num1} and {num2} is :{result} ")
                print("----------------------------------------------------------------------")
        #For Multiplication

        elif choice==3:
                result=num1*num2
                print("----------------------------------------------------------------------")
                print(f"The Multiplication of {num1} and {num2} is :{result} ")
                print("----------------------------------------------------------------------")
        #for Division
        elif choice==4:
                result=num1/num2
                print("----------------------------------------------------------------------")
                print(f"The Division of {num1} and {num2} is :{result} ")
                print("----------------------------------------------------------------------")
        #for Remainder
        elif choice==5:
                result=num1%num2
                print("----------------------------------------------------------------------")
                print(f"After dividing {num1} by {num2} the remainder is :{result} ")
                print("----------------------------------------------------------------------")
        
        elif choice==6:
                break
        else:
                print("You entered the wrong Operation")
                
                

