# password strenth caker
import re

def password_strength_caker(password):
    if len(password)<8:
        return "weak:password must atlest 8carecter"
    if not any(char.isdigit() for char in password):
        return"weak:password must be a degit"
    if not any(char.isupper() for char in password):
        return"weak:password must be contain a upper"
    if not any(char.islower() for char in password):
        return"weak:password must contain upper case"
    if not re.search (r'[~! @ # $ % ^ & * ( ) _ - + = { } | : ; "  < > , . ? ]',password):
        return"medium:password must contain a special carecter"
    return"strong:your pasword is sequre"
def main():
    print("wealcome to password strength cakker")
    while True:
        password=input("enter your password or type'exit' to exit this tool")
        if password.lower()=="exit":
            print("thakquu for using this tool")
            break
        result=password_strength_caker(password)
        print(result)

if __name__=="__main__":
    main()