import json
import re
from Projects import projects


# function for first and second name validation

def namevalidation():
    firstname = input("enter your first name : ").strip().lower()
    while True:
        if firstname.isalpha():
            lastname = input("enter your last name : ").strip().lower()
            if lastname.isalpha():
                break
            else:
                print("enter your last name without spaces or digits")
        elif firstname.isspace() or firstname.isalnum():
            print("enter your first name without spaces or digits")
            firstname = input("enter your first name : ").strip().lower()
    return [firstname, lastname]

# function for email validation

def emailvalidation():
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.com\b'
    email = input("enter your email : ").strip().lower()
    while True:
        if(re.fullmatch(regex, email)):
            break
        else:
            print("Invalid Email")
            email = input(
                "enter valid email contains @ and .com : ").strip().lower()
    return email

# function for password validation

def passwordvalidation():
    regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,18}$'
    password = input("enter your password : ").strip()
    while True:
        if(re.fullmatch(regex, password)):
            confirmedpassword = input("confirm your password : ").strip()
            if password != confirmedpassword:
                print("please confirm  your password , they are not the same")
            else:
                break
        else:
            print("Invalid password")
            password = input(
                "enter valid password contains uppercase , lowercase , number ,special character and al least 8 : ").strip().lower()
    return password

# function for phone validation

def phonevalidation():
    phone = input("please enter your number : ").strip().lower()
    while True:
        if len(phone) == 11 and phone.isnumeric():
            break
        else:
            print("please enter a valid egyptian number")
            phone = input("please enter your number : ").strip().lower()
    return phone

# main functions

# function for resgister

# def registration():
#     fullname = namevalidation()
#     with open("users.txt", 'a') as userfile:
#         userfile.writelines(
#             [f"{id(fullname)}:{fullname[0]}:{fullname[1]}:"])
#
#     email = emailvalidation()
#     with open("users.txt", 'a') as userfile:
#         userfile.write(f"{email}:")
#
#     password = passwordvalidation()
#     with open("users.txt", 'a') as userfile:
#         userfile.write(f"{password}:")
#
#     phone = phonevalidation()
#     with open("users.txt", 'a') as userfile:
#         userfile.write(f"{phone}\n")
#
#     print("your registration goes successfully")
#     choiceforlogin = input("do you want to login now?[y/n] ").strip().lower()
#     try:
#         choiceforlogin == "y" or choiceforlogin == "n"
#     except:
#         print("something went wrong")
#     else:
#         if choiceforlogin == "y":
#             login()
#         elif choiceforlogin == "n":
#             print("ok bye bye , hope to see you soon")
#         else:
#             print("invalid input")
# function for login


def registration():
    fullname = namevalidation()
    email = emailvalidation()
    password = passwordvalidation()
    phone = phonevalidation()

    user_data = {
        "id": id(fullname),
        "first_name": fullname[0],
        "last_name": fullname[1],
        "email": email,
        "password": password,
        "phone": phone
    }

    try:
        with open("users.json", 'r+') as userfile:
            users = json.load(userfile)
            users.append(user_data)
            userfile.seek(0)
            json.dump(users, userfile)
    except FileNotFoundError:
        with open("users.json", 'w') as userfile:
            json.dump([user_data], userfile)

    print("your registration goes successfully")
    # rest of the function...

# def login():
#     loginemail = input("please enter your email : ").strip().lower()
#     try:
#         with open("users.txt", 'r') as userfile:
#             data = userfile.read()
#             data = data.split(":")
#     except:
#         print("something went wrong")
#     else:
#         while True:
#             if loginemail in data:
#                 passuser = input("please enter your password : ").strip()
#                 if data[data.index(loginemail)+1] == passuser:
#                     print(
#                         f"welcome {data[data.index(loginemail)-2]} {data[data.index(loginemail)-1]}")
#                     try:
#                         projects(data[0])
#                     except:
#                         print("something went wrong")
#                     break
#                 else:
#                     print("Invalid password , try again")
#             else:
#                 print("Invalid email , try again")
#                 loginemail = input(
#                     "please enter your email : ").strip().lower()

# function for choose between login /register
def login():
    loginemail = input("please enter your email : ").strip().lower()
    try:
        with open("users.json", 'r') as userfile:
            users = json.load(userfile)
            user = next((u for u in users if u["email"] == loginemail), None)
            if user:
                passuser = input("please enter your password : ").strip()
                if user["password"] == passuser:
                    print(f"welcome {user['first_name']} {user['last_name']}")
                    # Call projects function here
                else:
                    print("Invalid password , try again")
            else:
                print("Invalid email , try again")
    except FileNotFoundError:
        print("No user data found.")

def signinup():
    choice = int(
        input("for login enter 1 _____ for register enter 2 : "))
    try:
        choice == 1 or choice == 2
    except:
        print("something went wrong")
    else:
        if choice == 1:
            try:
                login()
            except:
                print("something went wrong")
        elif choice == 2:
            try:
                registration()
            except:
                print("something went wrong")
        else:
            print("invalid choice")


signinup()