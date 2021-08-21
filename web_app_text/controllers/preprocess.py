#preprocess the data
# in preprocessing we perform stopword removal, character removal, lemmatization etc
from textblob import TextBlob
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from numpy import savetxt
import pandas as pd

nltk.download('stopwords')
nltk.download('wordnet')


def preprocess(tweet):
    tweet = re.sub(r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)", '', tweet)
    tweet = re.sub(r'<[^>]+>', '', tweet)
    tweet = re.sub(r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', '', tweet)
    tweet_blob = TextBlob(tweet)

    tweet_list = [ele for ele in tweet.split() if ele != 'user']
    clean_tokens = [t for t in tweet_list if re.match(r'[^\W\d]*$', t)]
    clean_s = ' '.join(clean_tokens)
    clean_mess = [word for word in clean_s.split() if word.lower() not in stopwords.words('english')]

    lem = WordNetLemmatizer()
    normalized_tweet = []
    for word in tweet_list:
        normalized_text = lem.lemmatize(word, 'v')
        normalized_tweet.append(normalized_text)
    return normalized_tweet




Final_words = []

'''
for data in new_df['Text']:
    filtered = preprocess(data)
    word_Final = ' '.join(filtered)
    Final_words.append(word_Final)

# store preprocessed data to new dataframe called final_bodyTrain

final_bodyTrain = pd.DataFrame(Final_words, columns=['body'])
'''
