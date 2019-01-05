import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from string import punctuation
from nltk.probability import FreqDist
from heapq import nlargest
from collections import defaultdict

#nltk.download('punkt')
#nltk.download('stopwords')

article_path = ('/Users/hernanrazo/pythonProjects/NLP_summarizer/article.txt')
stop_words = nltk.corpus.stopwords.words('english')
custom = ['?','(', ')', '.', '[', ']','!', '...',
';',"`","'",'"',',','-','$', "'s", "'ll", 'ca', "n't", "'m", "'re", "'ve"]
stop_words.extend(custom)


def open_file(article_path):

	try:
		with open(article_path, 'r') as file:
			return file.read()

	except IOError as e:
		print('Error trying to read file')


def clean_data():

	filtered_words = []
	filtered_sent = []

	data = open_file(article_path)
	data = data.lower()

	tokenized_words = nltk.word_tokenize(data)
	tokenized_sent = nltk.sent_tokenize(data)
	tokenized_words = [words for words in tokenized_words if not words in stop_words]

	for words in tokenized_words:
		if words not in stop_words:
			filtered_words.append(words)


	for words in tokenized_sent:
		if words not in stop_words:
			filtered_sent.append(words)

	return(filtered_words)
	return(filtered_sent)


#clean_data()
