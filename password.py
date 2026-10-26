valid=False

while not valid:
    password=input("Enter a password")
    if len(password)>=6 and any(char.isdigit() for char in password):
        valid=True
    else:
        print("Weak password... Try again")

if valid:
    print ("Strong")
