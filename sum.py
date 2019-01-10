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

#set stopwords with a few customs
stop_words = nltk.corpus.stopwords.words('english')
custom = ['?','(', ')', '.', '[', ']','!' ,
';',"`","'",'"',',','-',':','’', '$',"'s", 
"'ll", 'ca', "n't", "'m", "'re", "'ve"]
stop_words.extend(custom)

#set number of sentences for the summary
#Toggle this if you wish
length = 4

#set function for tokenization of words
def get_word_tokens():

	#open and read article 
	data = open(article_path, 'r').read()
	
	#set all letters to lowercase
	data = data.lower()

	#tokenize by individual words
	tokenized_words = word_tokenize(data)

	#filter out stopwords
	tokenized_words = [word for word in tokenized_words if word not in stop_words]

	return str(tokenized_words)

#set function to filter 
def get_sent_tokens():
	
	#open and read article
	data = open(article_path, 'r').read()
	
	#set all letters to lowercase
	data = data.lower()

	#tokenize by sentences
	tokenized_sent = sent_tokenize(data)

	#filter out stopwords
	tokenized_sent = [word for word in tokenized_sent if word not in stop_words]

	return str(tokenized_sent)

#calculate frequency distribution
def get_freq_dist(words):

	freq_dist = dict()

	#calculate the frequency of occurance for each word
	#incrementing its frequency by one everytime it occurs
	for word in words:
		if word in freq_dist:
			freq_dist[word] += 1
		else:
			freq_dist[word] = 1

	return freq_dist

#calculate the scores of each sentence
#TODO: make this better
def get_score(words, sentences, freq_dist):

	max_freq = max(freq_dist.values())
	sent_tokens = nltk.word_tokenize(sentences)

	score = {}
	#default = 'the'
	#freq_dist = freq_dist.get('the', default)

	for sentence in sentences:
		for word in sent_tokens:
			if sentence not in score.keys():
				score[sentence] = freq_dist[word]
			else:
				score[sentence] += freq_dist[word]

	return score
	

#define function that decides which sentences to 
#include in the summary
def get_summary(score, sentences, length):

	#create an index of scores
	index = nlargest(length, score, key=score.get)
	
	#rearrange the sentence in sorted order
	summary = [sentences[i] for i in sorted(index)]
	
	#join these sentences together into a shorter
	#version of the original article
	result = ' '.join(summary)

	return result

#call tokenization functions for words and sentences
words = get_word_tokens()
sentences = get_sent_tokens()


#call functions to get the frequency distribution and 
#the score for each sentence
freq_dist = get_freq_dist(words)
score = get_score(words, sentences, freq_dist)

#get the summary using the previously calculated values
summary = get_summary(score, sentences, length)

#write the resulting summary in a new txt file
#and save it locally
result = open(summary_path, 'w')
result.write(summary)
result.close()
print('done')

