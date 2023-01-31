
print('\n--------------- Section 3: Question 4 ---------------')
from collections import Counter

total_length = 0
unique_words = []

print('\n--------------- Section 3: Question 4 ---------------')
import operator
file = open("ai_trends.txt", "r")
exceptfile = open("stopwords_en.txt", "r")

data = file.read()
exceptdata = exceptfile.read()

words = []
freq = {}

dataList = data.replace('\n', " ").lower().split(" ")
exceptdatalist = exceptdata.replace('\n', " ").lower().split(" ")


for item in dataList:
    if item in exceptdatalist:
        continue
    words.append(item)

for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

#largest word
longest_word = ''
shortest_word = ''
for word in words:
    if len(word) > len(longest_word):
        longest_word = word
    else:
        len(word) < len(shortest_word)
        shortest_word = word

print(longest_word)
print(shortest_word)

#freq of words
sortedfreq = dict(sorted(freq.items(), key=operator.itemgetter(1),reverse=True))
print('\nFrequency of words in decending order:',sortedfreq)

#print the first 5 and last 5 entries
first = dict(list(sortedfreq.items())[0: 5])
print('\nThe 5 most frequent words',first)

last = dict(list(sortedfreq.items())[-5:])
print('\nThe 5 least frequent words',last)

occurrence_count = 0
for value in sortedfreq:
    occurrence_count += sortedfreq[value]
average_occurrence = round(float(occurrence_count)/float(len(sortedfreq)), 2)

print('The average occurrence of the words is:', average_occurrence)

print('\n--------------- Section 3: Question 5 ---------------')

from pandas import read_csv
data = read_csv("cars.csv")
print(data.head(3))
print(data.tail(3))
data["ratio"] = data["average-mileage"] / data["horsepower"]

sorted_df = data.sort_values(by='ratio')
sorted_df = sorted_df[0:5]


for item in sorted_df.index:
    print(str(sorted_df["car ID"][item]) + "-" + str(sorted_df["company"][item]) + "-" + str(sorted_df["body-style"][item]))