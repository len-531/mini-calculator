print("----------MINI-CALCULATOR----------")
while True:
    print("\nMenu")
    print("1.ADDITION")
    print("2.SUBTRACTION")
    print("3.MULTIPLICATION")
    print("4.DIVISION")
    op=int(input("Enter ur option: "))
    if op in [1, 2, 3, 4]:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
    if op==1:
        print("SUM: ",a+b)
    elif op==2:
        print("DIFFERENCE:",a-b)
    elif op==3:
        print("PRODUCT:",a*b)
    elif op==4:
        if b==0:
            print("NOT DEFINED")
        else:
            print("QUOTIENT: ",a/b)
    else:
        print("INVALID OPTION")
    ch=input("Do u want to continue y/n?:")
    if ch.lower() =='n':
        break