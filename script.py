import os
import string
from collections import Counter
import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from gensim.models.phrases import Phraser
from gensim.models import Phrases

#nltk.download('punkt')
#nltk.download('stopwords')


#set local paths for txt files containing the article and 
#another one for the created file where the summary will be printed onto
article_path = os.getcwd() + '/articles/article.txt'
summary_path = os.getcwd() + 'summaries/sum.txt'

stop_words = nltk.corpus.stopwords.words('english')
punctuation = list(string.punctuation)
lemma = WordNetLemmatizer()
stop = stop_words + punctuation 


def get_article(article):

    text = open(article).read()
    text = text.lower()

    return text


def split_sentences(sents):

    sentence_stream = [[i for i in word_tokenize(sent) if i not in stop_words] for sent in text]

    bigram = Phrases(sentence_stream, min_count = 2, threshold = 2, delimiter = b'_')
    bigram_phraser = Phraser(bigram)
    bigram_tokens = bigram_phraser[sentence_stream]

    trigram = Phrases(bigram_tokens, min_count = 2, threshold = 2, delimiter = b'_')
    trigram_phraser = Phraser(trigram)
    trigram_tokens = trigram_phraser[bigram_tokens]

    all_words = [i for j in trigram_tokens for i in j]
    freq_words = [i for i in Counter(all_words).most_common() if i[1] > 1]
    sentences = [i for i in trigram_tokens]

    return freq_words, sentences



def score_sentences(words, sentences):

    scores = Counter()

    for word in words:
        for i in range(0, len(sentences)):
            if word[0] in sentences[i]: 
                scores[i] += word[1]

    sentences_scores = sorted(scores.items(), key = scores.__getitem__, reverse = True)

    return sentence_scores


def get_summary(text, limit = 3):

    tokens = sent_tokenize(text)
    sentences = split_sentences(text)
    freq_words = split_sentences(text)
    sentence_scores = score_sentences(freq_words, sentences)

    scores = {sents[i]: sum(matrix[i]) for i in range(len(matrix))}
    sents = sorted(scores, key = scores.__getitem__, reverse = True)[:limit]
    best_sents = [i[0] for i in sorted([(i, text.find(i)) for i in sentences], key = lambda x: x[0])]

    return best_sents


def summarize(text, limit = 3):

    summary = get_summary(text, limit)
    print(' '.join(summary))






text = get_article(article_path)
summarize(text, 5)
