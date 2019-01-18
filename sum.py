import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from heapq import nlargest
from collections import defaultdict

#nltk.download('punkt')
#nltk.download('stopwords')

#set local paths for txt files containing the article and another one for the 
#created file where the summary will be printed onto
article_path = ('/Users/hernanrazo/pythonProjects/NLP_summarizer/article.txt')
summary_path = ('/Users/hernanrazo/pythonProjects/NLP_summarizer/sum.txt')

#set stop words to english and add some custom ones
stop_words = nltk.corpus.stopwords.words('english')
custom = ['?','(', ')', '.', '[', ']','!', '...',
';',"`","'",'"',',','$']
stop_words.extend(custom)

#set number of sentences for the summary
#toggle this if you wish
length = 4

def get_sent_tokens():

	filtered_sent = []
	
	data = open(article_path, 'r').read()
	data = data.lower()
	data = data.replace('\n', ' ')

	sent_tokens = nltk.sent_tokenize(data)

	for words in sent_tokens:
		if words not in stop_words:

			filtered_sent.append(words)

	return filtered_sent


def get_word_tokens():

	filtered_words = []

	data = open(article_path, 'r').read()
	data = data.lower()
	data = data.replace('\n', ' ')

	word_tokens = nltk.word_tokenize(data)

	for words in word_tokens:
		if words not in stop_words:

			filtered_words.append(words)

	return filtered_words




sentences = get_sent_tokens()
words = get_word_tokens()

print(sentences)
print(words)






