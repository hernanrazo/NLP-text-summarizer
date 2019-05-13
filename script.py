import os
import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from gensim.models import Phrases
from gensim.models.Phrases import Phraser

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


def sentence_intersect(s1, s2):

    sent1 = [i for i in word_tokenize(s1) if i not in stop_words]
    sent2 = [i for i in word_tokenize(s2) if i not in stop_words]
    intersect = [i for i in sent1 if i in sent2]
    inertsect_calc = (len(intersection) / (len(sent1) + len(sent2)) / 2)

    return intersect_calc

def sentence_split(sents):

    sentences = [[i for i in word_tokenize(sents) if i not in stop_words] for sent in sents]
    bigram = Phrases(sentences, min_count = 2, threshold = 2, delimiter = b'_')
    bigram_phraser = Phraser(bigram)
    bigram_tokens = bigram_phraser[sentences]
    trigram_phraser = Phraser(trigram)
    trigram_tokens = trigram_phraser[bigram_tokens]
    tokens = [i for i in trigram_tokens]

    return tokens









get_article(article_path)



