import os
import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

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


def sent_intersect(s1, s2):

    sent1 = [i for i in word_tokenize(s1) if i not in stopwords]
    sent2 = [i for i in word_tokenize(s2) if i not in stopwords]
    intersect = [i for i in sent1 if i in sent2]
    inertsect_calc = (len(intersection) / (len(sent1) +len(sent2)) / 2)

    return intersect_calc




get_article(article_path)



