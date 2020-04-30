# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 19:44:44 2020

@author: Tanvir
"""

# Packages & Libraries
import pandas as pd
import matplotlib.pyplot as plt
 
from os import walk
from os.path import join

import nltk
from nltk.stem import PorterStemmer
from nltk.stem import SnowballStemmer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

from bs4 import BeautifulSoup

# %matplotlib inline # This is anctually for Jupitar notbook specific for chart export

# Natural Language Processing
# Text Pre-Processing
msg = 'Hi I am Tanvir. Learning Data Science and this part is about NLP.'
msg.lower() # Convert all in lower case
msg.upper() # Convert all in upper case

# Download NLTK Resources (Tokenizer & Stopword)
nltk.download('punkt')
nltk.download('stopwords')

# Tokenising
msg = 'Hi I am Tanvir. Learning Data Science and this part is about NLP.'
word_tokenize(msg)

# If we need to tokenize all the string values to lower case
word_tokenize(msg.lower())


# Removing Stop Words
# get the list of stopwords dictionary and check the data type
type(stopwords.words('english'))

# Though it's a list type so we need to convert it to Set type and assign a variable
stopWords = set(stopwords.words('english'))
type(stopWords) # Just check the type of variavle

# To check a any particular word/s(string/s) in the stopWords
if 'this' in stopWords: print('Yes Got it')

# As a challenge: print 'Nope. Not in there.' if word 'hello'
if 'hello' not in stopWords: print('Nope. Not in there')

# Chellange: get the message and tokenize convert the lower case and remove the stop words from the sentance
testMsg = 'Hello I am Tanvir. Learning Data Science and try to build my future career in this sector'

word_tokenize(testMsg.lower())
type(word_tokenize(testMsg.lower()))

# decleare a variable and convert the tokenizeed words to the Set type
testMsgStopWords = set(word_tokenize(testMsg.lower()))
type(testMsgStopWords)

# For store the final result, need to introduce emplty list
filteredWords = []

# remove all the stop_words from the testMsg and store in the filteredWords
for word in testMsgStopWords:
    if word not in stopWords:
        filteredWords.append(word)
print(filteredWords)

# Word Stems and Stemming

# Get the message and tokenize convert the lower case and remove the stop words from the sentance
stemMsgWords = 'All works and no play makes Jack a dull boy. To be Not to be.'

word_tokenize(stemMsgWords.lower())

# Initiate PorterStremer to the variable
#stremmer = PorterStemmer() # This is the implementation of PorterStemmer
stremmer = SnowballStemmer('english') # This is the implementation of SnowballStemmer

type(word_tokenize(stemMsgWords.lower()))
# decleare a variable and convert the tokenizeed words to the Set type

stemMsgWords = set(word_tokenize(stemMsgWords.lower()))
type(stemMsgWords)

# For store the final result, need to introduce emplty list
filteredWords = []

# remove all the stop_words from the testMsg and store in the filteredWords
for word in stemMsgWords:
    if word not in stopWords:
        # define another variable 'stemmedWord' it will be address the result of stremmer
        stemmedWord = stremmer.stem(word)
        filteredWords.append(stemmedWord)
print(filteredWords)

# Removing Punctuation
# Get the message and tokenize convert the lower case and remove the stop words from the sentance
# To check is it the character or not python have a library to check as bellow
'P'.isalpha()
'?'.isalpha()

stemMsgWords = 'All works and no play makes Jack a dull boy. To be Not to be. ?? !!! ??'

word_tokenize(stemMsgWords.lower())

stremmer = SnowballStemmer('english') # This is the implementation of SnowballStemmer

type(word_tokenize(stemMsgWords.lower()))

stemMsgWords = set(word_tokenize(stemMsgWords.lower()))
type(stemMsgWords)

# For store the final result, need to introduce emplty list
filteredWords = []

# remove all the stop_words from the testMsg and store in the filteredWords
for word in stemMsgWords:
    if word not in stopWords and word.isalpha():
        # define another variable 'stemmedWord' it will be address the result of stremmer
        stemmedWord = stremmer.stem(word)
        filteredWords.append(stemmedWord)
print(filteredWords)



