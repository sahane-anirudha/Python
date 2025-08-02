

try:
    a=int(input("Enter the First Number: "))
    b=int(input("Enter the Second Number: "))

    print("What kind of operation do you want to perform? \n Press '+' to Addition \n Press '-' to Substraction  \n Press '*' to Multiplication \n Press '/' to Division")
    
    o=input("Enter the Operation")
    match o:
        case "+":
            print(f"The Result is :{a+b}")
        case "-":
            print(f"The Result is :{a-b}")
        case "*":
            print(f"The Result is :{a*b}")
        case "/":
            print(f"The Result is :{a/b}")  
        case default:
            print("There is an error")              

except Exception as e:
    print("Enter a Valid Value for a and b")


