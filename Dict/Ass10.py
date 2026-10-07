'''Q.10
Word Frequency
Write a Python program to take a sentence from the user and store each word and its frequency in a 
dictionary. Display the resulting dictionary.'''

sentence=input("Enter a sentence : ")

words=sentence.split()

d={}

for word in words:
    if word in d:
        d[word]+=1
    else:
        d[word]=1
        
print(d)
