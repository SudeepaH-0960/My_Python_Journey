# Calculation with integers 
a = int(input("Enter an integer value for a: "))
b = int(input("Enter an integer value for b: "))

print("Simple calculation results")
print("--------------------------")
sum = a + b
diff = a - b
product = a*b
division = a/b
floor_division = a//b
remainder = a%b
power = a**b
print(a,"+",b,"=",sum)
print(a,"-",b,"=",diff)
print(a,"x",b,"=",product)
print(a,"/",b,"=",division)
print(a,"//",b,"(floor division) =",floor_division)
print(a,"/",b,"(remainder) =",remainder)
print(a,"^",b,"=",power)

# Calculation with real numbers
x = float(input("Enter a real value for x: "))
y = float(input("Enter a real value for y: "))

print("Simple calculation results (without rounding off the digits)")
print("------------------------------------------------------------")
sum = x+y
diff = x-y
product = x*y
division = x/y
floor_division = x//y
remainder = x%y
power = x**y
print(x,"+",y,"=",sum)
print(x,"-",y,"=",diff)
print(x,"x",y,"=",product)
print(x,"/",y,"=",division)
print(x,"//",y,"(floor division) =",floor_division)
print(x,"/",y,"(remainder) =",remainder)
print(x,"^",y,"=",power)

# Rounding off the  results
print("Simple calculation results (rounding off the digits)")
print("----------------------------------------------------")
sum = round((x+y),2)
diff = round((x-y),2)
product = round((x*y),2)
division = round((x/y),2)
floor_division = round((x//y),2)
remainder = round((x%y),2)
power = round((x**y),2)
print(x,"+",y,"=",sum)
print(x,"-",y,"=",diff)
print(x,"x",y,"=",product)
print(x,"/",y,"=",division)
print(x,"//",y,"(floor division) =",floor_division)
print(x,"/",y,"(remainder) =",remainder)
print(x,"^",y,"=",power)