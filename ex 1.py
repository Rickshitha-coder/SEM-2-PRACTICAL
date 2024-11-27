print("Enter 'c' to convert from Celsius to  Fahrenheit")
print("Enter 'f' to convert from Fahrenheit to Celsius")
choice=input("Enter your choice:")
if choice=='c':
    celsius=float(input("Enter temperature in Celsius:"))
    fahrenheit=(celsius*9/5)+32
    print('%.2f Celsius is:%0.2f Fahrenheit'%(celsius,fahreheit))
elif choice==
