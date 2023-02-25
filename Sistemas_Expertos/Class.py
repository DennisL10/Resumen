import nltk
import urllib.request
import re
from inscriptis import get_text
from nltk import word_tokenize, sent_tokenize
import heapq
from googletrans import Translator

#nltk.download()

#
enlace = "https://en.wikipedia.org/wiki/Lake_Street_Transfer_station"
html = urllib.request.urlopen(enlace).read().decode('utf-8')
article_text = get_text(html)
article_text = article_text.replace("[ edigt ]", "")


article_text = re.sub(r'\[[0-9]*\]', ' ', article_text)
article_text = re.sub(r'\s+', ' ', article_text)

formatted_article_text = re.sub(r'[^a-zA-Z]', ' ', article_text)
formatted_article_text = re.sub(r'\s+', ' ', formatted_article_text)



sentence_list = nltk.sent_tokenize(article_text)

stopwords = nltk.corpus.stopwords.words('english')

word_frecuencies = {}
for word in nltk.word_tokenize(formatted_article_text):
    if word not in stopwords:
        if word not in word_frecuencies.keys():
            word_frecuencies[word] = 1
        else:
            word_frecuencies[word] += 1

maximun_frecuency = max(word_frecuencies.values())

for word in word_frecuencies.keys():
    word_frecuencies[word] = (word_frecuencies[word]/maximun_frecuency)



#CALCULA LAS FRASES QUE MAS SE REPITEN 
sentence_score = {}
for sent in sentence_list:
    for word in nltk.word_tokenize(sent.lower()):
        if word in word_frecuencies.keys():
            if len(sent.split(' ')) < 30:
                if sent not in sentence_score.keys():
                    sentence_score[sent] = word_frecuencies[word]
                else:
                    sentence_score[sent] += word_frecuencies[word]

#REALIZAR RESUMEN CON LAS MEJORES FRASES
summary_sentences = heapq.nlargest(7, sentence_score, key=sentence_score.get)
summary = ' '.join(summary_sentences)

translator = Translator()
trad = translator.translate(summary, dest='spanish')
print(trad.text)




