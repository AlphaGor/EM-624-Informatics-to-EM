# Author: Ashutosh Laxminarayan Gor

# importing all the required libraries:
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
from urllib.request import urlopen
from bs4 import BeautifulSoup
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import nltk

# https://www.cnn.com/sport

# Getting the target url:
cnn = urlopen("https://www.cnn.com/sport")
soup = BeautifulSoup(cnn,'html.parser')
headlines = soup.find('body').find_all('h3')
# print('\n')


# Processing the stopword file:
stop_list = open('stopwords_en.txt','r',encoding= 'utf8', errors= 'ignore')
stop_list1 = [word for line in stop_list for word in line.split()]
# print(stop_list1)

# Creating Lists of headlines:
sentiment = {}
headlines_list = []
print('These are the headlines captured from the news website:')
for x in headlines:
    headline = x.text.strip()
    print(headline)
    word_list = headline.split(" ")
    for word in word_list:
        if(word.isalpha()):
            tempword = word
            for stop in stop_list1:
                if word.lower() == stop.lower():
                    word_list.remove(word)
        else:
            word_list.remove(word)
    word_list = ' '.join(word_list)
    # print(word_list)
    headlines_list.append(word_list)


# Removing all the non-alphabetical elements:
char_list = ['€', '!', '%',"\"","/", "'",'"', ':', ';', '?', '@', '#', '$', '(', ')', '[', ']', '<', '>', '{', '}', '&',
             '1', '2','3', '4', '5', '6', '7', '8', '9', '0', ',', '.', '-', "'re", "'ve", "'s", "'t", "'ll", "'d"]
headlines_list = [i for i in headlines_list if all(ch not in i for ch in char_list) and len(i) > 3]

# Removing all the frequently used/repeated words:
freq_word = ['fans','gets','get','play','told','the','some','be','an','and','also','like','look','a','says','in','cast',
             'and','like','what','universe','on','about','than','to','the','there','them','that','from',
             'include','following','years','annual']
headlines_list1 = [i for i in headlines_list if i not in freq_word]

# Analyzing the sentiment of the list of headlines:
sentiment = SentimentIntensityAnalyzer()
clean_headlines_str = ' '.join(headlines_list1)
vad_sentiment = sentiment.polarity_scores(clean_headlines_str)

pos = vad_sentiment['pos']
neg = vad_sentiment['neg']
neu = vad_sentiment['neu']

print('\nThe headlines are rated accordingly:'
      '\n''{:.1%}'.format(pos), "headlines have positive sentiment",
      '\n''{:.1%}'.format(neg), "headlines have negative sentiment &",
      '\n''{:.1%}'.format(neu), "headlines have neutral sentiment.")

# Creating a new string & Printing the headlines with highest and lowest sentiment:
min_ele, max_ele = headlines_list1[2], headlines_list1[2]
for i in range(1, len(headlines_list1)):
    if headlines_list1[i] < min_ele:
        min_ele = headlines_list1[i]

    if headlines_list1[i] > max_ele:
        max_ele = headlines_list1[i]
print('\nMost positive & most negative headlines in the data:')
print(min_ele)
print(max_ele)

# Extracting bigram from the headlines:
head_line = clean_headlines_str
headline_token = nltk.word_tokenize(head_line)
headline_bigram = list(nltk.bigrams(headline_token))
# print(headline_bigram)
headlines_bigram = [('_'.join(a)) for a in headline_bigram]
print('\nThese are the bigrams extracted from the llist of headlines:'
      '\n',headlines_bigram)

# Creating word cloud for the list of headlines extract from the bigrams:
plt.figure(figsize=(10, 10))
print("\nWordcloud for the list of headlines:",)
wordcloud_pro = WordCloud(width=800, height=800, background_color='white', max_words=100).generate(clean_headlines_str)
plt.imshow(wordcloud_pro)
plt.axis("off")
plt.title("Word Cloud for the list of headlines:", fontsize=10)
plt.tight_layout(pad=0)
plt.show()
