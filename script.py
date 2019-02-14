import spacy 
from spacy.lang.en.stop_words import STOP_WORDS


article_path = ('/Users/hernanrazo/pythonProjects/NLP_summarizer/article.txt')
summary_path = ('/Users/hernanrazo/pythonProjects/NLP_summarizer/sum.txt')

nlp = spacy.load('en_core_web_sm')

nlp.Defaults.stop_words |= {'?','(', ')', '.', '[', ']','!', 'th',';',"`","'",'"',',','$', '/'}

length = 4


def get_word_tokens(path):
    
    filtered_words = []

    file = open(path, 'r')
    data = file.read()
    file.close()

    data = data.lower()
    datta = data.replace('\n', ' ')

    doc = nlp(data)

    for word in doc:
        if word.is_stop == False:
            filtered_words.append(word)

    return filtered_words

    
def get_sent_tokens(path):

    filtered_sent = []
    
    words = get_word_tokens(path)

    sentences = (''.join(str(words)))

    for sentence in sentences:
        filtered_sent.append(sentence)

    return filtered_sent


#sent = ('%s' % ''.join(map(str, sentences)))

#sent = (''.join(list(chain.from_iterable(sentences))))

    



#words = get_word_tokens(article_path)
#print(words)

sentences = get_sent_tokens(article_path)

print(sentences)




