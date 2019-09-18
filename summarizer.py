import os
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from coolections import defaultdict
from string import punctuation
from heapq import nlargest

#nltk.download('punkt')
#nltk.download('stopwords')


#set local paths for txt files containing the article and
#another one for the created file where the summary will be printed onto
article_path = os.getcwd() + '/articles/article.txt'
summary_path = os.getcwd() + 'summaries/sum.txt'

stop_words = nltk.corpus.stopwords.words('english')
punctuation = list(string.punctuation)
stop = stop_words + punctuation


class FrequencySummarizer:

    def __init__(self, min_cut = 0.1, max_cut = 0.9):

        self.min_cut = min_cut
        self.max_cut = max_cut
        self.stopwords = set(stopwords.words('english') + list(punctuation))

    def compute_frequencies(self, word_sent):

        freq - defaultdict(int)

        for s in word_sent:
            for word in s:
                if word not in self._stopwords:
                    freq[word] += 1

        m = float(max(freq.values()))

        for w in freq.keys():
            freq[w] = freq[w]/m

            if freq[w] >= self._max_cut or freq[w] <= self._min_cut:
                del freq[w]

        return freq

    def summarize(self, text, n):

        sents = sent_tokenize(text)
        assert n <= len(sents)
        word_sent = [word_tokenize(s.lower()) for s in sents]
        self._freq = self._compute_frequencies(word_sent)
        ranking = defaultdict(int)
        for i, sent in enumerate(word_sent):
            for w in sent:
                if w in self._freq:
                    ranking[i] += self._freq[w]
        sent_idx = self._rank(ranking, n)

        return [sents[j] for j in sents_idx]

    def _rank(self, ranking, n):

        return nlargest(n, ranking, key=ranking.get)

