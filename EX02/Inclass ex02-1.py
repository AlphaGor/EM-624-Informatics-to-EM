while True:
    inputone = int(input("Please enter a number or 'done' to stop the process : "))
    if inputone == 'done':
        break
    if inputone % 2 == 0:
        print(inputone, "is an even number. ")
    else:
        print(inputone, "is an odd number. ")
    if inputone % 2 == 0:
        print(inputone, "is a multiple of 2. ")
    else:
        print(inputone, "is not a multiple of 2. ")
    if inputone % 4 == 0:
        print(inputone, "is a multiple of 4. ")
    else:
        print(inputone, "is not a multiple of 4. ")