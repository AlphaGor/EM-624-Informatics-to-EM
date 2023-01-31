# Author : Ashutosh Laxminarayan Gor

# importing necessary pakages:
import nltk
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Opening the text files:
pro_list = open('space_pros.txt','r', encoding= 'utf8', errors= 'ignore')
con_list = open('space_cons.txt','r',encoding= 'utf8', errors= 'ignore')
stop_list = open('stopwords_en.txt','r',encoding= 'utf8', errors= 'ignore')

# Using data to change into lowercases:
pro_list1 = [word.lower() for line in pro_list for word in line.split()]
con_list1 = [word.lower() for line in con_list for word in line.split()]
stop_list1 = [word for line in stop_list for word in line.split()]

# Getting stop words from the data:
pro_list_1 = [i for i in pro_list1 if i not in stop_list]
con_list_1 = [i for i in con_list1 if i not in stop_list]

# Sorting data with minimum length of 3 alphabets:
char_list = ['€', '!', '%',"\"","/", "'",'"', ':', ';', '?', '@', '#', '$', '(', ')', '[', ']', '<', '>', '{', '}', '&', '1', '2',
             '3', '4', '5', '6', '7', '8', '9', '0', ',', '.', '-', "'re", "'ve", "'s", "'t", "'ll", "'d"]
pro = [i for i in pro_list_1 if all(ch not in i for ch in char_list) and len(i) > 3]
con = [i for i in con_list_1 if all(ch not in i for ch in char_list) and len(i) > 3]

# Sorting data for most frequently used words:
freq_word = ['space','colonies','planets','humans','aliens','galaxy','moon',"'",'"','and','like','what','universe','on',
             'to','the','there','them','that','from','include','following','years','galaxy']

pro_list11 = [i for i in pro if i not in freq_word]
con_list11 = [i for i in con if i not in freq_word]

# Doing sentimental Analysis:
analyzer = SentimentIntensityAnalyzer()
clean_pro_str = ' '.join(pro_list11)
vad_sentiment = analyzer.polarity_scores(clean_pro_str)

pos = vad_sentiment['pos']
neg = vad_sentiment['neg']
neu = vad_sentiment['neu']

print('\nThe sentiment behind cleaned PRO file of Space Colonization:')
print('\nThe pro text file is rated as:', '{:.1%}'.format(pos), "Positive", '{:.1%}'.format(neg), "Negative &",
      '{:.1%}'.format(neu), "Neutral")

clean_con_str = ' '.join(con_list11)
vad_sentiment1 = analyzer.polarity_scores(clean_con_str)

pos1 = vad_sentiment1['pos']
neg1 = vad_sentiment1['neg']
neu1 = vad_sentiment1['neu']

print('\nThe sentiment behind the cleaned CON file of Space Colonization :')
print('\nThe con text is rated as:', '{:.1%}'.format(pos1), "Positive", '{:.1%}'.format(neg1), "Negative &",
      '{:.1%}'.format(neu1), "Neutral")


# Tokenization of data:
word_pro = clean_pro_str
pro_token = nltk.word_tokenize(word_pro)

# Creating Bigram for pros(Positive):
freq_dist = nltk.FreqDist(pro_token).most_common(5)
print('\nThe 5 most frequent used words in the PRO file are:', freq_dist)
pro_bigram = list(nltk.bigrams(pro_token))
print('\nBigrams extracted from the cleaned PRO text:')
print(pro_bigram)

# Creating Bigram for cons(Negative):
word_con = clean_con_str
con_token = nltk.word_tokenize(word_con)

freq_dist1 = nltk.FreqDist(con_token).most_common(5)
print('\nThe 5 most frequently used words in the CON file:', freq_dist1)
con_bigram = list(nltk.bigrams(con_token))
print('\nBigrams extracted from the cleaned CON text:')
print(con_bigram)

# Creating WordCloud for Pros file:
plt.figure(figsize=(10, 10))
print("\nWordcloud for PRO file (1st) and CON file (2nd):", )
wordcloud_pro = WordCloud(width=900, height=900, background_color='white', max_words=100).generate(clean_pro_str)
plt.imshow(wordcloud_pro)
plt.axis("off")
plt.title("Word Cloud for Pro file:", fontsize=10)
plt.tight_layout(pad=0)
plt.show()

# Creating WordCloud for Cons file:
plt.figure(figsize=(10, 10))
wordcloud_con = WordCloud(width=900, height=900, background_color='white', max_words=100).generate(clean_con_str)
plt.imshow(wordcloud_con)
plt.axis("off")
plt.title("The CON file word cloud", fontsize=10)
plt.tight_layout(pad=0)
plt.show()
