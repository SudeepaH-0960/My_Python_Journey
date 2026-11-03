# Usage of conditional operators in if..elif..else statement
x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")


# Usage of logical operator with if..else statement
if x > y or x < y:
    print("x is not equal to y")
else:
    print("x is equal to y")


# Usage of logical operator with if..elif..else statement
score = int(input("Score(0-100): "))

if 90 < score <= 100:
    print("Grade: O")
elif 80 < score <= 90:
    print("Grade: A+")
elif 70 < score <= 80:
    print("Grade: A")
elif 60 < score <= 70:
    print("Grade: B")
elif 50 < score <= 60:
    print("Grade: C")
elif 40 < score <= 50:
    print("Grade: D")
else:
    print("Grade: F")


# Odd or Even
x = int(input("What's x? "))
if x%2 == 0:
    print("x is even")
else:
    print("x is odd")


# The Boolean data type
def main():
    x = int(input("Enter x: "))
    if is_even(x):
        print("x is even")
    else:
        print("x is odd")

def is_even(k):
    return k%2 == 0    # It returns a boolean value: True or False

main()

# Multiple logical operators in single if statement
name = input("Enter the name: ")
if name == "Ram" or name == "Sham" or name == "Rohit":
    print("Bellary")
elif name == "Tejas":
    print("Shimoga")
else:
    print("Unknown identity")
    