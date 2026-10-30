# Calculation of integers 
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
sum = a + b
diff = a - b
product = a*b
division = a/b
print(a,"+",b,"=",sum)
print(a,"-",b,"=",diff)
print(a,"x",b,"=",product)
print(a,"/",b,"=",division)

# Calculation of float values
x = float(input("Enter the value of x: "))
y = float(input("Enter the value of y: "))

sum = x+y
diff = x-y
product = x*y
division = x/y
print(x,"+",y,"=",sum)
print(x,"-",y,"=",diff)
print(x,"x",y,"=",product)
print(x,"/",y,"=",division)

# Rounding off the  results
sum = round((x+y),2)
diff = round((x-y),2)
product = round((x*y),2)
division = round((x/y),2)
print(x,"+",y,"=",sum)
print(x,"-",y,"=",diff)
print(x,"x",y,"=",product)
print(x,"/",y,"=",division)
