import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from string import punctuation
from nltk.probability import FreqDist
from heapq import nlargest
from collections import defaultdict

#nltk.download('punkt')
#nltk.download('stopwords')
#nltk.download('vader_lexicon')

article_path = ('/Users/hernanrazo/pythonProjects/NLP_summarizer/article.txt')
stop_words = nltk.corpus.stopwords.words('english')

print('it worked')