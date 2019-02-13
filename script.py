import spacy 
from spacy.lang.en.stop_words import STOP_WORDS



article_path = ('/Users/hernanrazo/pythonProjects/NLP_summarizer/article.txt')
summary_path = ('/Users/hernanrazo/pythonProjects/NLP_summarizer/sum.txt')

nlp = spacy.load('en_core_web_sm')

nlp.Defaults.stop_words |= {'?','(', ')', '.', '[', ']','!', 'th',';',"`","'",'"',',','$', '/'}

length = 4

def get_sent_tokens(path):

    filtered_sent = []

    file = open(path, 'r')
    data = file.read()
    file.close()

    data = data.lower()
    data = data.replace('\n', ' ')

    doc = nlp(data)
    
    
            
    return filtered_sent
    

def get_word_tokens(path):
    
    filtered_words = []

    file = open(path, 'r')
    data = file.read()
    file = close()

    data = data.lower()
    datta = data.replace('\n', ' ')

    doc = nlp(data)

    for word in doc:
        if word.is_stop == False:
            filtered_words.append(word)

    return filtered_words

    









sentences = get_sent_tokens(article_path)
print(sentences)


