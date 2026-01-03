print("----------MINI-CALCULATOR----------")
print("Menu")
print("1.ADDITION")
print("2.SUBTRACTION")
print("3.MULTIPLICATION")
print("4.DIVISION")
a=int(input("Enter first input: "))
b=int(input("Enter second input: "))
op=int(input("Enter ur option: "))
if op==1:
    print("SUM OF",a,"and",b,"IS",a+b)
elif op==2:
    print("DIFFERENCE OF",a,"and",b,"IS",a-b)
elif op==3:
    print("PRODUCT OF",a,"and",b,"IS",a*b)
elif op==4:
    if b==0:
        print("NOT DEFINED")
    else:
        print("QUOTIENT OF",a,"and",b,"IS",a/b)
else:
    print("INVALID OPTION")