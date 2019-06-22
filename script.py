import os
import string
from collections import Counter
import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from gensim.models.phrases import Phraser

#nltk.download('punkt')
#nltk.download('stopwords')


#set local paths for txt files containing the article and 
#another one for the created file where the summary will be printed onto
article_path = os.getcwd() + '/articles/article.txt'
summary_path = os.getcwd() + 'summaries/sum.txt'

stop_words = nltk.corpus.stopwords.words('english')
punctuation = list(string.punctuation)
lemma = WordNetLemmatizer()
stop = stop_words + punctuation 

def get_article(article):

    text = open(article).read()
    return text

def clean_data(text):

    filtered_text = []
    text = text.lower()
    tokenized_lyrics = nltk.word_tokenize(text)
    filtered_lyrics = [words for words in tokenized_lyrics if not words in stop_words]

    for words in tokenized_lyrics:
        if words not in stop_words:
            filtered_text.append(words)

    return filtered_text




def intersection(sent1, sent2):
    s1 = sent1.split(' ')
    s2 = sent2.split(' ')

    intersection = [i for i in s1 if i in s2]
    #Normalization
    return len(intersection) / ((len(s1) + len(s2)) / 2)

def get_summary(text, limit = 3):

    sentences = sent_tokenize()


text = get_article(article_path)
'''
sentences = sent_tokenize(text)
matrix = [[intersection(sentences[i], sentences[j]) for i in range(0,len(sentences))] for j in range(0,len(sentences))]


scores = {sentences[i]: sum(matrix[i]) for i in range(len(matrix))}
sents = sorted(scores, key = scores.__getitem__, reverse = True)[:5]


tuples = [(i, text.find(i)) for i in sents]
sorted_tuples = sorted(tuples, key = lambda x: x[0])

best_sents = [i[0] for i in sorted_tuples]

print(best_sents)
'''

cleaned_text = clean_data(text)
print(cleaned_text)



