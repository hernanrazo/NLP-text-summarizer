import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from heapq import nlargest
from collections import defaultdict
import re

#nltk.download('punkt')
#nltk.download('stopwords')

#set local paths for txt files containing the article and another one for the 
#created file where the summary will be printed onto
article_path = ('/Users/hernanrazo/pythonProjects/NLP_summarizer/article.txt')
summary_path = ('/Users/hernanrazo/pythonProjects/NLP_summarizer/sum.txt')

#set stop words to english and add some custom ones
stop_words = nltk.corpus.stopwords.words('english')
custom = ['?','(', ')', '.', '[', ']','!', 'th',
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

	return str(filtered_sent)

def get_word_tokens():

	filtered_words = []

	data = open(article_path, 'r').read()

	data = data.lower()
	data = data.replace('\n', ' ')
	data = re.sub('[^a-zA-Z]', ' ', data)
	data = re.sub(r'\s+', ' ', data)

	word_tokens = nltk.word_tokenize(data)

	for words in word_tokens:
		if words not in stop_words:

			filtered_words.append(words)

	return filtered_words


def get_freq_dist(words):

	freq = {}

	for word in words:
		if word not in freq.keys():
			freq[word] = 1
		else:
			freq[word] += 1

	#max_freq = max(freq.values())

	#for word in freq.keys():
	#	freq[word] = (freq[word] / max_freq)

	return freq

def get_score(sentences, freq_dist):

	scores = {}
	words = nltk.word_tokenize(sentences)

	for sent in sentences:
		for word in words:
			if word in freq_dist.keys():
				if sent not in scores.keys():
					scores[sent] = freq_dist[word]

				else:
					scores[sent] += freq_dist[word]

	return scores





sentences = get_sent_tokens()
words = get_word_tokens()
freq_dist = get_freq_dist(words)

scores = get_score(sentences, freq_dist)

print(sentences)
print(words)
print(freq_dist)
print(scores)

word_list = []
sent_list = []

for sent in sentences:
	for word in words:
		word_list.append(word)
		sent_list.append(sentences)
print('================================')
print(word_list)
print('================================')

print(sent_list)



