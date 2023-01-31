# Author : Ashutosh Laxminarayan Gor
#Part 1:
import csv
count = 0
with open("NYC-CitiBike-Jan_Feb2016.csv", 'r') as infile1:
    print("\n These are the last five lines in the file: ")
    for rows in (infile1.readlines()[-5:]):
        print(rows, end=' ')
print("\n")

with open("NYC-CitiBike-Jan_Feb2016.csv", 'r') as infile1:
    reader = csv.reader(infile1, delimiter=',')
    usertype1 = -1
    subscriber1 = 0
    customer1 = 0

    for row in reader:
        if (usertype1 == -1):
            usertype1 = 0
            continue
        usertype1 += 1

        if (row[13] == 'Subscriber'):
            subscriber1 += 1
        if (row[13] == 'Customer'):
            customer1 += 1
percent1 = float(customer1) / int(usertype1) * 100

print('The file has', usertype1, 'lines.', customer1, 'of them have "Customer" as usertype,', subscriber1,
      'have "Subscriber" as usertype. Customer are', percent1, '% of the total.')
print("\n")

#Part 2:
count = 0
with open("NYC-CitiBike-Apr_May2016.csv", 'r') as infile2:
    print("\n These are the first five lines in the file: ")
    next(infile2)
    for line in infile2:
        print(line)
        count += 1
        if count == 5:
            break
print("\n")

with open("NYC-CitiBike-Apr_May2016.csv", 'r') as infile2:
    reader = csv.reader(infile2, delimiter=',')
    usertype2 = -1
    subscriber2 = 0
    customer2 = 0

    for row in reader:
        if (usertype2 == -1):
            usertype2 = 0
            continue
        usertype2 += 1

        if (row[13] == 'Subscriber'):
            subscriber2 += 1
        if (row[13] == 'Customer'):
            customer2 += 1
percent2 = float(customer2) / int(usertype2) * 100

print('The file has', usertype2, 'lines, of which', customer2,'have "Customer" as usertype,',subscriber2,'have "Subscriber" as usertype. Customer are',percent2 ,'% of the total.')

if usertype1>usertype2:
    print("The first file is bigger than the second one.")
else:
    print("\n The first file is smaller than the second file.")
if percent1>percent2:
    print("The first file has relatively more customers than the second one.")
else:
    print("The first file has relatively less customers than the second file.")

#Part 3:
if usertype1>usertype2:
    print("\nThere are more riders in winter compared to the number of riders during the spring.")
else:
    print("\nThere are more riders in spring compared to the number of riders during the winter.")
if percent1>percent2:
    print("During the Winter there are more Customers than in the Spring")
else:
    print("During the Winter there are more non-Subscribers than in the Spring")

print("\n Run by Ashutosh Laxminarayan Gor")
print("Thank You for using the tool :)")