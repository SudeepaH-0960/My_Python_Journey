# Defining a simple function 
def greeting(to):
    print("hello,",to)
name = input("Enter your name: ")
greeting(name)

# Mini calculator
def calci(a,b):
    sum = a+b
    diff = a-b
    product = a*b
    div = a/b
    print(a,"+",b,"=",sum)
    print(a,"-",b,"=",diff)
    print(a,"*",b,"=",product)
    print(a,"/",b,"=",div)
a = int(input("Enter an integer value for 'a': "))
b = int(input("Enter an integer value for 'b': "))
calci(a,b)

# The 'return' value
def square(a):
    return a**2
num = int(input("Enter a number to get its squares: "))
print(square(num))  # We should use print() here because 'return' does not print the result or command

# Function inside a function
def BMI():   # BMI -> Body Mass Index
    w = float(input("Enter your weight(in kg): "))
    h = float(input("Enter your height(in m)"))
    print("Your Body Mass Index is:",bmi_value(w,h))
def bmi_value(w,h):
    return round((h**2),2)
BMI()