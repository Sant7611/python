name = input("Enter your  name: ")

template = f"Dear <|{name}|>, \nYou are selected \n<|Date|>"

print(template)

print(name.find("  "))