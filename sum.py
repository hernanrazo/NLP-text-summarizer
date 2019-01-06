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

def main():

	article = open_file(article_path)
	sentence_length = 6
	sentence_data = clean_data(article)
	word_data = clean_data(article)
	sentence_scores = scoring(sentence_data, word_data)
	summary = get_summary(sentence_scores, sentence_data, sentence_length)

	return summary


def open_file(article_path):

	try:
		with open(article_path, 'r') as file:
			return file.read()

	except IOError as e:
		print('Error trying to read file')


def clean_data(article):

	data = open_file(article_path)
	data = data.lower()

	tokenized_words = nltk.word_tokenize(data)
	
	
	return [nltk.sent_tokenize(data), [word for word in data if word not in stop_words]]


def scoring(filtered_words, filtered_sent):

	word_frequency = FreqDist(filtered_words)

	scoring = defaultdict(int)

	for i, sentence in enumerate(filtered_sent):
		for words in word_tokenize(sentence.lower()):
			if words in word_frequency:

				scoring[i] += word_frequency[words]

	return scoring

def get_summary(scores, sentence, length):

	indexes = nlargest(length, scores, key=scores.get)
	final_sentence = [sentence[j] for j in sorted(indexes)]
	summary = ' '.join(final_sentence)
	
	return summary


if __name__ == "__main__":

	print(main())
