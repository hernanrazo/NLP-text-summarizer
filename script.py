import os
import string
from collections import Counter
import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from gensim.models.phrases import Phraser
from gensim.models import Phrases

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
    text = text.lower()

    return text

def intersection(sent1, sent2):

    intersection = [i for i in sent1 if i in sent2]
    normalize = len(intersection) / ((len(sent1) + len(sent2)) / 2)

    return normalize


def split_sentences(text):

    sentence_stream = [[i for i in word_tokenize(sent) if i not in stop_words] for sent in text]

    bigram = Phrases(sentence_stream, min_count = 2, threshold = 2, delimiter = b'_')
    bigram_phraser = Phraser(bigram)
    bigram_tokens = bigram_phraser[sentence_stream]

    trigram = Phrases(bigram_tokens, min_count = 2, threshold = 2, delimiter = b'_')
    trigram_phraser = Phraser(trigram)
    trigram_tokens = trigram_phraser[bigram_tokens]
    result = [i for i in trigram_tokens]

    return result



def get_summary(text, limit = 3):

    sentences = split_sentences(text)
    matrix = [[intersection(sentences[i], sentences[j]) for i in range(0, len(sentences))] for j in range(0, len(sentences))]

    scores = {text[i]: sum(matrix[i]) for i in range(len(matrix))}
    sentences = sorted(scores, key = scores.__getitem__, reverse = True)[:limit]
    best_sents = [i[0] for i in sorted([(i, text.find(i)) for i in sentences], key = lambda x: x[0])]

    return best_sents



text = get_article(article_path)

split = split_sentences(text) #shit isnt splitting right
print(split)
'''
summary = get_summary(text)

print(' '.join(summary))


'''
