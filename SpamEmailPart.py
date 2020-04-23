# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 01:11:16 2020

@author: Tanvir
"""
# Packages & Libraries 


# List of Constants, whihc will not be changes
exampleFile = 'SpamData/01_Processing/practice_email.txt'

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







