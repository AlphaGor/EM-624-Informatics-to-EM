# Author: Ashutosh Laxminarayan Gor
import pandas as pd
import operator
import datetime

df1 = pd.read_csv("JC-201611-citibike-tripdata.csv")
df2 = pd.read_csv("JC-202111-citibike-tripdata.csv")
print('\n ********** Processing file JC-201611-citibike-tripdata.csv **********')


def print_details(dataframe):
    duration = []
    depart = {}
    for i in range(len(dataframe)):
        duration.append(dataframe[i][0])
        # 4 8
    duration_avg2 = sum(duration) / len(duration)
    print("\n Average trip duration in November 2016 is", int(duration_avg2),'Seconds')

listoflist_df1 = df1.values.tolist()
print_details(listoflist_df1)

def print_details(dataframe):
    duration = []
    depart = {}
    for i in range(len(dataframe)):

        duration.append(dataframe[i][0])

        if dataframe[i][4] in depart:
            depart[dataframe[i][4]] += 1
        else:
            depart[dataframe[i][4]] = 1

    startpt1 = dict(sorted(depart.items(), key=operator.itemgetter(1), reverse=True)[:5])
    print('\n The 5 most popular starting stations in November 2016:', startpt1)
    return startpt1

listoflist_df1 = df1.values.tolist()
stpt1 = print_details(listoflist_df1)

def print_details(dataframe):
    duration = []
    depart = {}
    for i in range(len(dataframe)):

        duration.append(dataframe[i][0])

        if dataframe[i][8] in depart:
            depart[dataframe[i][8]] += 1
        else:
            depart[dataframe[i][8]] = 1

    endpt1 = dict(sorted(depart.items(), key=operator.itemgetter(1), reverse=True)[:5])
    print('\n The 5 most popular ending stations in November 2016:', endpt1)
    return endpt1

listoflist_df1 = df1.values.tolist()
edpt1 = print_details(listoflist_df1)

user1 = df1[(df1['User Type'] == 'Subscriber')]
u1 = len(user1)
print('\n Total number of subscribers:', u1)

user2 = df1[(df1['User Type'] == 'Customer')]
u2 = len(user2)
print('\n Total number of Customers:', u2)

total1 = u1 + u2
print('\n Total number of users in November 2016:', total1)

print('\n ********** Processing file JC-202111-citibike-tripdata.csv **********')

def print_details1(dataframe):
    time = []
    for i in range(len(dataframe)):
        start_date = listoflist_df2[i][2]
        end_date = listoflist_df2[i][3]

        start = datetime.datetime(int(start_date[:4]), int(start_date[5:7]), int(start_date[8:10]),
                                  int(start_date[11:13]), int(start_date[14:16]), int(start_date[17:19]))
        end = datetime.datetime(int(end_date[:4]), int(end_date[5:7]), int(end_date[8:10]),
                                int(end_date[11:13]), int(end_date[14:16]), int(end_date[17:19]))
        diff = end - start
        seconds = diff.total_seconds()
        time.append(int(seconds))
    # print(time)
    duration_avg1 = sum(time) / len(time)
    print("\n Average trip duration in November 2021 is", int(duration_avg1),'Seconds')

listoflist_df2 = df2.values.tolist()
print_details1(listoflist_df2)

def print_details(dataframe):
    duration = []
    depart = {}
    for i in range(len(dataframe)):

        duration.append(dataframe[i][0])

        if dataframe[i][4] in depart:
            depart[dataframe[i][4]] += 1
        else:
            depart[dataframe[i][4]] = 1

    startpt2 = dict(sorted(depart.items(), key=operator.itemgetter(1), reverse=True)[:5])
    print('\n The 5 most popular starting stations in November 2021:', startpt2)
    return startpt2

listoflist_df2 = df2.values.tolist()
stpt2 = print_details(listoflist_df2)

def print_details(dataframe):
    duration = []
    depart = {}
    for i in range(len(dataframe)):

        duration.append(dataframe[i][0])

        if dataframe[i][6] in depart:
            depart[dataframe[i][6]] += 1
        else:
            depart[dataframe[i][6]] = 1

    endpt2 = dict(sorted(depart.items(), key=operator.itemgetter(1), reverse=True)[:5])
    print('\n The 5 most popular ending stations in November 2021:', endpt2)
    return endpt2
listoflist_df2 = df2.values.tolist()
edpt2 = print_details(listoflist_df2)

user3 = df2[(df2['member_casual'] == 'member')]
u3 = len(user3)
print('\n Total number of members:', u3)
user4 = df2[(df2['member_casual'] == 'casual')]
u4 = len(user4)
print('\n Total number of casuals:', u4)
total2 = u3 + u4
print('\n Total number of users in November 2021:', total2)

print('\n ********** Comparing both the files **********')


if u1>u3:
    print('\n The total number of members are more in November 2016 than November 2021 ')
else:
    print('\n The total number of members are more in November 2021 than November 2016 ')

if u2>u4:
    print('\n The total number of Casual users are more in November 2016 than November 2021 ')
else:
    print('\n The total number of Casual users are more in November 2021 than November 2016 ')

if total1>total2:
    print('\n The average trip duration is more in November 2016 than November 2021 ')
else:
    print('\n The average trip duration is more in November 2021 than November 2016 ')

ridership = total2 - total1
print('\n The ridership change over the 5 years shows that there is an increase of',ridership,'in total number of users.')

print('\n This is the end of the files processing.')
print('\n Run by: Ashutosh Laxminarayan Gor')