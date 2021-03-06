from urllib import request
from bs4 import BeautifulSoup
import nltk
from nltk import wordpunct_tokenize, pos_tag, ne_chunk
from nltk.stem import WordNetLemmatizer
from nltk import everygrams
from nltk.stem import PorterStemmer

#site url    
url = "https://en.wikipedia.org/wiki/Google"
html = request.urlopen(url).read().decode('utf8')
#use beatiful soup for scraping
soup = BeautifulSoup(html, "html.parser") 
#get the title
title = soup.find('title')
#create input file
result = open("input.txt",'w')
#find everything that have <p> 
body = soup.find_all('p')
#find the text, we will use this text for the other tasks
text = soup.getText()
    
#write on to the file
for i in body:
    result.writelines(str(i)+'\n')
        

#tokenizing text
stokens = nltk.sent_tokenize(text)
print(stokens)
#pos
pos = nltk.word_tokenize(text)
print(nltk.pos_tag(pos))

#stemming the text
stemmer = PorterStemmer()
print(stemmer.stem(text))

#trigram
nltk.download('words')
nltk.download('maxent_ne_chunker')
nltk.download('averaged_perceptron_tagger')

print(list(everygrams(text.split(), 1, 5)))

#lemmentization
nltk.download('wordnet')
lemm = WordNetLemmatizer()
print(lemm.lemmatize(text))

#named entity recognition
ner = ne_chunk(pos_tag(wordpunct_tokenize(text)))
print(ner)