#Author: Ashutosh Laxminarayan Gor
print("\n Run by Ashutosh Laxminarayan Gor")

inputOne = input("How many US Dollars do you want to exchange : ")

while(inputOne.isdigit() == False):
    print("\n Error : Input must be a numerical value.")
    inputone = input("How many US Dollars do you want to exchange : ")

    inputOne = inputone

inputTwo = input("Enter the name of the currency you are converting dollars into : ")
inputThree = input("What is the Exchange rate? ")

while(inputThree.isdigit() == False):
    print("\n Error : Input must be a numerical value.")
    inputthree = input("What is the Exchange rate?  ")
    inputThree = inputthree

print('\nYou can exchange', inputOne, 'U.S. Dollars for', float(inputOne) * int(inputThree), inputTwo )

