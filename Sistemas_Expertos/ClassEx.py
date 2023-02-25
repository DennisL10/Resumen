import nltk
import urllib.request
import re
from inscriptis import get_text
from nltk import word_tokenize, sent_tokenize
import heapq
from googletrans import Translator

#nltk.download()

#
texto = "The Lake Street Transfer station was a rapid transit station on the Chicago , serving as a transfer station between its Lake Street Elevated Railroad and the Logan Square branch of its Metropolitan West Side Elevated Railroad. Located where the Logan Square branch crossed over the Lake Street Elevated, it was in service from 1913 to 1951, when it was rendered obsolete by the construction of the Dearborn Street subway. The transfer station was an amalgamation of two predecessor stations: Wood, on the Lake Street Elevated, was on Wood Street, one block west of the site of the future transfer, and had been constructed in 1893; the Metropolitan's Lake station, on the other hand, was on the site of the future transfer and had been built in 1895. These stations, and their lines, had been constructed by two different companies; when they and two more companies building what would become the merged operations in the early 1910s, a condition for the merger was the construction of a transfer station between the Metropolitan and Lake Street Elevateds at their crossing, which in practice meant the replacement of Wood station with a new Lake Street one under the Metropolitan. Having already merged operations, the companies formally united under the Chicago Rapid Transit Company (CRT) in 1924; the became publicly owned when the Chicago Transit Authority (CTA) assumed operations in 1947. Plans for a subway to provide a more direct route from Logan Square to downtown dated to the late 1930s, but the subway was originally intended to supplement the Logan Square branch of the area, on which the Metropolitan's station lay, rather than replace it. The newly formed CTA, however, found little reason to continue operation of the old Logan Square elevated. The subway was completed in 1951, leading to the station's closing, but remnants survived into the 1960s. The site of the station is near the junction of the Paulina Connector  the descendant of the old Logan Square trackage – and the Lake Street Elevated, which was used for temporary and non-revenue service until the Pink Line opened in 2006 and returned it to revenue status. Lake Street Transfer was double-decked, the Metropolitan's tracks and station located immediately above the Lake Street's tracks and station. Access to the eastbound Lake Street platform was by a station house at the street level; passengers would then use the platform to access the Metropolitan's platforms and Lake Street's westbound platform by additional stairways. The Metropolitan West Side Elevated Railroad Company, another founding company of the Chicago , was granted a fifty-year franchise by the Chicago City Council on April 7, 1892.[11] Unlike the Lake Street Elevated, which operated a single line, the Metropolitan had a main line that proceeded west from downtown to Marshfield Junction, where it split into three branches: one northwestern branch to Logan Square (which in turn had a branch to Humboldt Park[d]), one branch due west to Garfield Park, and one southwestern branch to Douglas Park.[15] While the competing South Side and Lake Street Elevateds used steam traction, the Metropolitan never did; although it had originally intended to, and indeed had built much of its structure under the assumption that locomotives would be used,[16] it decided in May 1894 to have electrified tracks instead,[17] making it upon its opening the first revenue electric elevated railroad in the United States.[18] The Metropolitan's tracks on the Logan Square branch[d] were finished up to Robey by the middle of October 1894, and were powered on in April 1895 for test and inspection runs.[12] The Metropolitan began service at 6:00 a.m. on Monday, May 6, 1895, between Robey on the Logan Square branch and Canal on the main line.[19] Eleven stations opened that day, one of which was on Lake Street.[19] Since the Lake station crossed the Lake Street Elevated, its tracks and platforms were much higher than elsewhere"





sentence_list = nltk.sent_tokenize(texto)

stopwords = nltk.corpus.stopwords.words('english')

word_frecuencies = {}
for word in nltk.word_tokenize(texto):
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