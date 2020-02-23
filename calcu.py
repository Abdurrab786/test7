
print("select operation")
print("1.add")
print("2.sub")
print("3.mul")
print("4.div")

choice=input("enter the operator")
num1=float(input("enter the first number"))
num2=float(input("enter the second number"))
if choice =='1':
    print(num1,"+",num2,"=", add(num1,num2))
    elif choice =='2':
        print(num1,"-",num2,"=", sub(num1,num2))
         elif choice =='3':
             print(num1,"*",num2,"=", mul(num1,num2))
              elif choice =='4':
                  print(num1,"/",num2,"=", div(num1,num2))
                  else:
                      print("onvalid input")
        
