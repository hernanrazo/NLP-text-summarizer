import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
import heapq
from heapq import nlargest
import re
import spacy



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


nlp = spacy.load('en_core_web_sm')

def get_sent_tokens(path):

	file = open(path, 'r')
	data = file.read()
	file.close()

	data = data.lower()
	data = data.replace('\n', ' ')

	doc = nlp(data)

	sentences = [sent.string.strip() for sent in doc.sents]

	return sentences



#def get_word_tokens(path):





sentences = get_sent_tokens(article_path)

print(sentences)

































































'''
def get_sent_tokens(path):

	filtered_sent = []
	
	file = open(path, 'r')
	data = file.read()
	file.close()

	data = data.lower()
	data = data.replace('\n', ' ')

	sent_tokens = nltk.sent_tokenize(data)

	for words in sent_tokens:
		if words not in stop_words:

			filtered_sent.append(words)

	return str(filtered_sent)

def get_word_tokens(path):

	filtered_words = []

	file= open(path, 'r')
	data = file.read()
	file.close()

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
		#freq[word] = (freq[word] / max_freq)

	return freq

def get_score(sentences, freq_dist):

	scores = {}
	words = nltk.word_tokenize(sentences)

    for i, sentences in enumerate(sentences):
    
        for word in words:
            if word in freq_dist:
                score[i] += freq_dist[word]

	return scores


def get_summary(length, sentences, words, score):
    
    summary = heapq.nlargest(length, scores, key=scores.get)
    full_summary = ' '.join(summary)

    return full_summary



sentences = get_sent_tokens(article_path)
words = get_word_tokens(article_path)
freq_dist = get_freq_dist(words)
#scores = get_score(sentences, freq_dist)
#summary = get_summary(length, sentences, words, scores)







#print(scores)
#print(summary)

#sent = ('%s' % ''.join(map(str, sentences)))

#sent = (''.join(list(chain.from_iterable(sentences))))

'''

