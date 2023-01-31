import pandas as pd
import operator
import datetime
import csv
df1 = pd.read_csv("JC-201611-citibike-tripdata.csv")

user = df1[(df1['User Type'] == 'Subscriber')]

print(len(user))