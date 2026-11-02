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

if score > 90 and score <= 100:
    print("Grade: O")
elif score > 80 and score <= 90:
    print("Grade: A+")
elif score > 70 and score <= 80:
    print("Grade: A")
elif score > 60 and score <= 70:
    print("Grade: B")
elif score > 50 and score <= 60:
    print("Grade: C")
elif score > 40 and score <= 50:
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