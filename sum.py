import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from heapq import nlargest
from collections import defaultdict

#nltk.download('punkt')
#nltk.download('stopwords')

article_path = ('/Users/hernanrazo/pythonProjects/NLP_summarizer/article.txt')
stop_words = nltk.corpus.stopwords.words('english')
custom = ['?','(', ')', '.', '[', ']','!' ,
';',"`","'",'"',',','-',':','’', '$', "'s", "'ll", 'ca', "n't", "'m", "'re", "'ve"]
stop_words.extend(custom)


def get_word_tokens():

	data = open(article_path, 'r').read()
	data = data.lower()

	tokenized_words = word_tokenize(data)
	tokenized_words = [word for word in tokenized_words if word not in stop_words]

	return tokenized_words

def get_sent_tokens():

	data = open(article_path, 'r').read()
	data = data.lower()

	tokenized_sent = sent_tokenize(data)
	tokenized_sent = [word for word in tokenized_sent if word not in stop_words]

	return tokenized_sent


def get_freq_dist(words):

	freq_dist = dict()

	for word in words:
		if word in freq_dist:
			freq_dist[word] += 1
		else:
			freq_dist[word] = 1

	return freq_dist

def get_score(sentences, freq_dist):

	sent_value = dict()

	#this is all wrong
	for sentence in sentences:
		for word_value in freq_dist:
			if sentence[:12] in sent_value:
				sent_value[sentence[:12]] += word_value[1]
			else:
				sent_value[sentence[:12]] = word_value[1]






words = get_word_tokens()
sentences = get_sent_tokens()

get_freq_dist(words)








