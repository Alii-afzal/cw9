import re

def validation_password():
    
    while True:
        password = input("Enter your password: ")
        if re.findall(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,}$", password):
            print("correct passwrod")
            exit()
        else : 
            print("incoreect password!!!")
        
validation_password()