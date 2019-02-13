import spacy 
from spacy.lang.en.stop_words import STOP_WORDS



article_path = ('/Users/hernanrazo/pythonProjects/NLP_summarizer/article.txt')
summary_path = ('/Users/hernanrazo/pythonProjects/NLP_summarizer/sum.txt')

length = 4

nlp = spacy.load('en_core_web_sm')

def get_sent_tokens(path):

    file = open(path, 'r')
    data = file.read()
    file.close()

    data = data.lower()
    data = data.replace('\n', ' ')

    doc = nlp(data)
    
   # sentences = [sent.string.strip() for sent in doc.sent]
    
    for word in doc:
        if word.is_stop == False:
            





    return sentences
    






print(STOP_WORDS)


sentences = get_sent_tokens(article_path)
print(sentences)


