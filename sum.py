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

length = 5

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

def get_score(words, sentences, freq_dist):

	score = defaultdict(int)

	for counter, sentence in enumerate(sentences):
		for word in words:
			if word in freq_dist:
				score[counter] += freq_dist[word]

	return score

def get_summary(score, sentences, length):

	index = nlargest(length, score, key=score.get)
	summary = [sentences[i] for i in sorted(index)]
	result = ' '.join(summary)

	return result


words = get_word_tokens()
sentences = get_sent_tokens()

freq_dist = get_freq_dist(words)

score = get_score(words, sentences, freq_dist)

summary = get_summary(score, sentences, length)
#clean this and put in a new txt file??
print(summary)

