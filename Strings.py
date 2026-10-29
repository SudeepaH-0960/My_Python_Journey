name = input("Enter your name: ")

# 1.Printing name in different ways
print("hello,")
print(name)

print("hello," + name)
print("hello, " + name)
print("hello,", name)

# <1.1> Using print() function's parameters
print("hello,", end='')
print(name)
print("hello,", end=' ')
print(name)
print("hello,",name, sep='')
print("hello,",name,sep=' ')
print(f"hello, {name}")

# <1.2> Using some strings methods

# Removing whitespace from name
name = name.strip()
print(f"hello, {name}")

# Capitalizing name (Only first letter of first word)
name = name.capitalize()
print(f"hello, {name}")

# Capitalizing name (First letter of each word)
name = name.title()
print(f"hello, {name}")

# Combining methods
name = name.strip().title()
print(f"hello, {name}")

# Can also add in the initial input command
user_name = input("Enter your name: ").strip().title()
print(f"hello, {user_name}")

# 2. Escape Characters
# Next line character
print("Hello, users.\nThis is the second line.")

# Tab space
print("Hello, users.\tLet us dive into the concepts.")

# Single and Double quotes
print("Ram said \'Hi\' to Sham. Sham replied back as \"Hello\".")