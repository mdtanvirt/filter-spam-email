# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 01:11:16 2020

@author: Tanvir
"""
# Packages & Libraries
import pandas as pd
import matplotlib.pyplot as plt
 
from os import walk
from os.path import join

# %matplotlib inline # This is anctually for Jupitar notbook specific for chart export

# List of Constants, whihc will not be changes
exampleFile = 'SpamData/01_Processing/practice_email.txt'

spamPath1 = 'SpamData/01_Processing/spam_assassin_corpus/spam_1'
spamPath2 = 'SpamData/01_Processing/spam_assassin_corpus/spam_2'
easyNonSpamPath1 = 'SpamData/01_Processing/spam_assassin_corpus/easy_ham_1'
easyNonSpamPath2 = 'SpamData/01_Processing/spam_assassin_corpus/easy_ham_2'

dataJsonFile = 'SpamData/01_Processing/emailTextData.json'

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

# Data cleaning: Checking for missing values
# Checking if any message bodies are null
# data.MESSAGE # Show the messages infos of email body
data['MESSAGE'] # Another way to show the same result

# To check any of the message values is null
#data['MESSAGE'].isnull()
data.MESSAGE.isnull()
data.MESSAGE.isnull().values  # Show only values
data.MESSAGE.isnull().values.any() # To show any value is null in entire messages

# Missing value is not the same thing of Empty Message the empty message string is line " "
type("") # This actually show the emplty string
len("") # This will shows the length of empty string

myEmptyVar = None # Define the empty veriable
type(myEmptyVar) # Check the variable type

# Check if there are empty emails (string length is ziro)
data.MESSAGE.str.len()

# To check any of the value is 0
data.MESSAGE.str.len() == 0

# To check any rows is True
(data.MESSAGE.str.len() == 0).any()

# Count the number of email body contain 0
(data.MESSAGE.str.len() == 0).sum()

# Challenge: how would you check the number of entries will null/None values?
data.MESSAGE.isnull().any().sum()

# Locate empty emails
type(data.MESSAGE.str.len())

data[data.MESSAGE.str.len() == 0].index

# To get or locate the row number where the cmds lives (It's a type of searching features)
data.index.get_loc('cmds')

# Though 'cmds' is the system files so we have to remore those files from the dataset
# Remove System file entities from the data frame
data = data.drop(['cmds']) # This will update the dataframe in "data" - way-1 (Overwrite)
#data.drop(['cmds'], inplace=True) # way-2

data.shape

# Add documents ID to track Emails Dataset
documentIDs = range(0, len(data.index)) # here range is set from 0 to total number of emails
# To check the ranges
documentIDs

# Create new column in dataset and put the specific number for each record from the in range
data['DOCID'] = documentIDs
data.DOCID # Check the new column value 


# Save to File using Pandas
data.to_json(dataJsonFile)

# Number of Spam messages visualised (Pie Charts)
data.CATEGORY.value_counts()

countOfSpamMsg = data.CATEGORY.value_counts()[1]
countofHamMsg = data.CATEGORY.value_counts()[0]

categoryName = ['Spam', 'Legit Mail']
slizeOfPie = [countOfSpamMsg, countofHamMsg]
customColor = ['#ff7675', '#74b9ff']

plt.figure(figsize=(2, 2), dpi=200)
plt.pie(slizeOfPie, labels = categoryName, textprops={'fontsize':6}, 
        startangle=70, autopct='%1.2f%%', colors=customColor, explode=[0, 0.1])
plt.show()















