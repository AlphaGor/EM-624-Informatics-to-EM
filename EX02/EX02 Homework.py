print("\n Run by Ashutosh Laxminarayan Gor. ")

print("\n Password must contain at least 5 characters but not more than 12. ")
print(" Password can be any combination of alphabetical and numerical characters. ")
print(" Password must also contain at least one uppercase, one lowercase & one numerical characters. ")
choice = "yes"

while(choice == 'yes'):
    digit = 0
    lower = 0
    upper = 0

    password = input("\n Please enter your password for validation: ")

    if len(password) < 5 :
        print("Password must contain minimum 5 characters. ")
        continue

    elif len(password) > 12 :
        print("Password must not contain more than 12 characters. ")
        continue

    for char in password:
        if((char.isdigit()) == True):
            digit += 1
        elif((char.islower()) == True):
            lower += 1
        elif((char.isupper()) == True):
            upper += 1

    if(digit == 0):
        print(" 'ERROR', Your password must contain a numerical character. ")

    if(upper == 0):
        print(" 'ERROR', Your password must contain an uppercase alphabetic character. ")

    if(lower == 0):
        print(" 'ERROR', Your password must contain a lowercase alphabetic character. ")

    if(digit != 0 and upper != 0 and lower !=0):
        print("\n Your password has been validated. ")
        choice = input("Do you want to continue? (enter 'done' to stop or 'yes' to continue):")

    if(choice == 'done'):
        print( ")"\n Thank you for using this tool! :)