

digit = 0
upper = 0
lower = 0
special = 0
    # $ # @ len 6 - 12
passsword = input("input please")
if (len(passsword) >=12):
    for Char in passsword:
        if i.islower():
            lower +=1
        continue

        el i.isupper():
            upper +=1
        continue

        elif i.isdigit():
            digit += 1
        continue

        elif (i=='@' or i=='#' or i=='$'):
            special +=1
        continue

        print("pass")
else:
    print(fail)