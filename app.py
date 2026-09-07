def register():
    global name,email,password
    name=input("Input name : ")
    while True:
        email=input("Input email : ")
        if "@" in email:
            break
        else:
            print("@")
    while True:
        password=input("Input password : ")
        has_upper=False
        has_lower=False
        has_number=False
        for char in password:
            if char.isupper():
                has_upper = True
            if char.islower():
                has_lower = True
            if char.isdigit():
                has_number = True
        if len(password) < 8:
            print("Password must be at least 8 characters")
        elif has_upper == False:
            print("Password must contain uppercase")
        elif has_lower == False:
            print("Password must contain lowercase")
        elif has_number == False:
            print("Password must contain a number")
        else:
            break
        print("register successfully")
def login():
    login_email=input("Input email : ")
    login_password=input("Input password : ")
    if login_email==email and login_password==password:
        print("login successfully")
    else:
        print("email and password are not match")
while True:
    print('--------Menu------')
    print('1. Register')
    print('2. Login')
    print('3. Exit')
    opt=input("Input option (1-3) : ")
    if opt=="1":
        register()
    elif opt=="2":
        pass
    elif opt=="3":
        break
    else:
        print("invalid number")