# textcapitalizer
print("⟦⟦TEXT CAPITALIZER⟧⟧")


text = input("\n→Enter Some text Here→:")

print("1.🔍uppercase")
print("2.🔡lowercase")
print("3.🆙capitalize")
print("4.↗️Title case")

choice = input("🤔Choose a format between [1-4] :")

if choice == "1":
    print(text.upper())
elif choice == "2":
    print(text.lower())
elif choice == "3":
    print(text.capitalize())
elif choice == "4":
    print(text.title())
