sentence=input("Enter you full name: ")
wordcount=1
lettercount=0
for i in sentence:
    lettercount=lettercount+1
    if i == " ":
        wordcount=wordcount+1
        lettercount=lettercount-1
print(wordcount)
print(lettercount)