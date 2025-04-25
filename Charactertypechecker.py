print("Character Type Checker")


char = input("Enter a single character:")


if char.isdigit():
    print("This is a Number")
elif char.isalpha():
    print("This is a letter")
else:
    print("This is a special character")
