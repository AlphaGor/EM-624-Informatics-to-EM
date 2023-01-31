# Author: Ashutosh Laxminarayan Gor
import pandas as pd
from collections import Counter
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Read file into dataframe
news = pd.read_csv('News_2021.csv')

# Cleaning the unwannted blank spaces:
news['content'] = news['content'].fillna(' ')
news['description'] = news['description'].fillna(' ')

# Creating a new column containing the description and content of each article
news['description&content'] = news.apply(lambda row: ' '.join((row['description'], row['content'])), axis=1)

def related_to_covid(string):
    covid_words = ['covid', 'vaccine', 'coronavirus', 'moderna', 'pfizer', 'johnson','vaccination', 'antibody']
    related = False
    for word in string.strip().split():
        word = word.lower()
        if word in covid_words:
            related = True
    return(related)

# Creating a new column to determine if each file is related to Covid 19
news['Related_to_covid'] = news.apply(lambda x: related_to_covid(x['description&content']), axis=1)

def clean_description(string):
    stopwords_file = open('stopwords_en.txt', 'r')
    stopwords = []
    for word in stopwords_file:
        stopwords.append(word.strip())
    clean_words = []
    for word in string.strip().split():
        word = word.lower()
        if word.isalpha() and word not in stopwords and len(word) > 3:
            clean_words.append(word)
    return(clean_words)

# Creating a column to hold the cleaned text:
news['Cleaned_c&d'] = news.apply(lambda x: clean_description(x['description&content']), axis=1)

# Creating a list of all the words in every article:
all_words = []
for list in news['Cleaned_c&d']:
    all_words = all_words + list

# Creating dataframe to hold only covid articles:
covid_news = news[news['Related_to_covid'] == True]
# Creating list to hold words from all articles:
covid_words = []
for list in covid_news['Cleaned_c&d']:
    covid_words = covid_words + list

# Creating dataframe to hold only non-covid articles:
non_covid_news = news[news['Related_to_covid'] == False]
# Create list to hold words from non-covid articles
non_covid_words = []
for list in non_covid_news['Cleaned_c&d']:
    non_covid_words = non_covid_words + list


# 20 most common words used in file:
most_frequent = Counter(all_words).most_common(20)
common_dict = dict(most_frequent)
print('\nThese are the 20 most common words used in all the news articles:\n')
print(common_dict)

# Calculating the percentage of articles related to COVID-19:
no_covid_articles = len(news[news['Related_to_covid'] == True])
no_total_articles = len(news['Related_to_covid'])
prcnt_related_to_covid = no_covid_articles/no_total_articles*100

print(f'\nPercent of articles relate to COVID-19: {prcnt_related_to_covid:.2f}% ({no_covid_articles}/{no_total_articles})')
print('\nThese are the COVID-19 related news articles:')
print(covid_news['title'])

# Doing sentimental Analysis:
analyzer = SentimentIntensityAnalyzer()
clean_covid_str = ' '.join(non_covid_words)
vad_sentiment = analyzer.polarity_scores(clean_covid_str)

pos = vad_sentiment['pos']
neg = vad_sentiment['neg']
neu = vad_sentiment['neu']

print('\nAll the non COVID-19 related news articles are rated as:', '{:.1%}'.format(pos),
      "Positive", '{:.1%}'.format(neg), "Negative &", '{:.1%}'.format(neu), "Neutral")

clean_word_str = ' '.join(all_words)
vad_sentiment = analyzer.polarity_scores(clean_word_str)

pos = vad_sentiment['pos']
neg = vad_sentiment['neg']
neu = vad_sentiment['neu']

print('\nAll the news articles are rated as:', '{:.1%}'.format(pos), "Positive", '{:.1%}'.format(neg), "Negative &",
      '{:.1%}'.format(neu), "Neutral")

# Creating word cloud for all words in all the articles
plt.figure(figsize=(10, 10))
wordcloud_1 = WordCloud(height=1000, width=1000, background_color='white', max_words=1000).generate(' '.join(all_words))
plt.imshow(wordcloud_1)
plt.axis("off")
plt.title("Word Cloud for all the news articles:", fontsize=10)
plt.tight_layout(pad=0)
plt.show()

# Creating word cloud for all words in non COVID related articles
plt.figure(figsize=(10, 10))
wordcloud_2 = WordCloud(height=1000, width=1000, background_color='white', max_words=1000).generate(' '.join(non_covid_words))
plt.imshow(wordcloud_2)
plt.axis("off")
plt.title("Word Cloud for non COVID-19 related news articles:", fontsize=10)
plt.tight_layout(pad=0)
plt.show()
