secret_password = "group55"
user_pass =""

tries = 3

while tries > 0 and user_pass != secret_password:
    user_pass = input('enter paswrod ( you have' str(tries) + "left:")

    tries = tries - 1

    if user_pass == secret_password:
        print("acces granted")
    elif tries == 0:
        print("you dont have any tries")
    else:
        print("access denied, try again")