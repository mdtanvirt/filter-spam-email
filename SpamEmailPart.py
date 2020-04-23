# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 01:11:16 2020

@author: Tanvir
"""
# Packages & Libraries
import pandas as pd
 
from os import walk
from os.path import join

# List of Constants, whihc will not be changes
exampleFile = 'SpamData/01_Processing/practice_email.txt'

spamPath1 = 'SpamData/01_Processing/spam_assassin_corpus/spam_1'
spamPath2 = 'SpamData/01_Processing/spam_assassin_corpus/spam_2'
easyNonSpamPath1 = 'SpamData/01_Processing/spam_assassin_corpus/easy_ham_1'
easyNonSpamPath2 = 'SpamData/01_Processing/spam_assassin_corpus/easy_ham_2'

spamCat = 1
hamCat = 0

# Reading file - Way 1
stream = open(exampleFile, encoding='latin-1')  # File open and store as 'stream'
message = stream.read()                         # Read all the message from the file and store it as "message"
stream.close()                                  # For stop reading message

print(message)


# Reading file - Way 2
stream2 = open(exampleFile, encoding='latin-1')
isBody = False
lines = []

for line in stream2:
    if isBody:
        lines.append(line)
    elif line == '\n':
        isBody = True

stream2.close()

# print(lines)
emailBody = '\n'.join(lines)
print(emailBody)

# Generator Function (Understanding)
def generateSqares(N):
    for myNumbers in range(N):
        yield myNumbers ** 2
        
for i in generateSqares(5):
    print(i, end=' ->')

# Email body extraction

def emailBodyGenerator(path):
    for root, dirnames, filenames in walk(path):
        
        for fileName in filenames:
            
            filepath = join(root, fileName)
            
            stream3 = open(filepath, encoding='latin-1')
            isBody = False
            lines = []
            
            for line in stream3:
                if isBody:
                    lines.append(line)
                elif line == '\n':
                    isBody = True
            
            stream3.close()
            
            # print(lines)
            emailBody = '\n'.join(lines)
            yield fileName, emailBody
            
def dfFromFirectory(path, classification):
    rows = []
    rowsNames = []
    
    for fileName, emailBody in emailBodyGenerator(path):
        rows.append({'MESSAGE' : emailBody, 'CATEGORY' : classification})
        rowsNames.append(fileName)
    
    return pd.DataFrame(rows, rowsNames)

spamEmails = dfFromFirectory(spamPath1, 1)
spamEmails = spamEmails.append(dfFromFirectory(spamPath2, 1))
spamEmails.head()

spamEmails.shape

hamEmails = dfFromFirectory(easyNonSpamPath1, hamCat)
hamEmails = hamEmails.append(dfFromFirectory(easyNonSpamPath2, hamCat))
hamEmails.head()

hamEmails.shape

data = pd.concat([spamEmails, hamEmails])
print('Shape of entore data frame is: ', data.shape)
data.head()

data.tail()