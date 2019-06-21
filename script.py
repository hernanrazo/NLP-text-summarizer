import os
from collections import Counter
import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from gensim.models.phrases import Phraser


#nltk.download('punkt')
#nltk.download('stopwords')

#set local paths for txt files containing the article and 
#another one for the created file where the summary will be printed onto
article_path = os.getcwd() + '/articles/article.txt'
summary_path = os.getcwd() + 'summaries/sum.txt'

#set stopwords
stop_words = nltk.corpus.stopwords.words('english')


def get_article(article):

    text = open(article).read().lower()
    return text

print(get_article(article_path))
