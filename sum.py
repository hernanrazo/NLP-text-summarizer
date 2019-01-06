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
custom = ['?','(', ')', '.', '[', ']','!'  ,
';',"`","'",'"',',','-',':','’', '$', "'s", "'ll", 'ca', "n't", "'m", "'re", "'ve"]
stop_words.extend(custom)

def main():

	words = get_word_tokens()
	print(words)

	sentences = get_sent_tokens()
	print(sentences)

	score = get_score(words, sentences)

	print(score)


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


def get_score(words, sentences):

	word_frequency = FreqDist(words)

	score = defaultdict(int)

	for i, sentence in enumerate(sentences):
		for word in nltk.word_tokenize(sentences):
			if word in word_frequency:
				score[i] += word_freq[word]

	return score


if __name__ == "__main__":

	main()
