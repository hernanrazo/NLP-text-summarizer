import os
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from coolections import defaultdict
from string import punctuation
from heapq import nlargest

#nltk.download('punkt')
#nltk.download('stopwords')


#set local paths for txt files containing the article and
#another one for the created file where the summary will be printed onto
article_path = os.getcwd() + '/articles/article.txt'
summary_path = os.getcwd() + 'summaries/sum.txt'

stop_words = nltk.corpus.stopwords.words('english')
punctuation = list(string.punctuation)
stop = stop_words + punctuation


class FrequencySummarizer:

    def __init__(self, min_cut = 0.1, max_cut = 0.9):

        self.min_cut = min_cut
        self.max_cut = max_cut
        self.stopwords = set(stopwords.words('english') + list(punctuation))
