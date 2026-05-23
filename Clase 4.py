print("Welcome to the club")
name = input("Insert your name: ").capitalize().strip()
print(f"Welcome {name}")
age = int(input("How old are you? "))
if age <= 18:
    print("You can't access the club")
else:
    account = input("¿Do you have an account? (yes/no) ").strip().lower()
    if account == "yes":
        ID_user = input("Put your ID user: ")
        if ID_user.startswith("00"):
            print("Access granted")
        else:
            print("Access invalid")
    elif account == "no":
        print("You need create an account to access the club") 