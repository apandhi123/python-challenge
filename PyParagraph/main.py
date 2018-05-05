# Modules
import os

# Set file path
txtpath = "C:\\Users\\apandhi\\Desktop\\UTAUS201804DATA2-Class-Repository-DATA\\03-Python\\HOMEWORK\\Instructions\\PyParagraph\\raw_data\\paragraph_1.txt"

# Set file path

# Set all variables to default
num_words = 0
lines = 0
sentences = 0
num_chars = 0

with open(txtpath) as paragraph:
   #Find out word count
   #print (paragraph.read())
   for line in paragraph:
       words = line.split()
       num_words += len(words)
       num_chars += len(line)
        
       lines += 1
       if line.startswith('\n'):   
            blanklines += 1
       else:
    # assume that each sentence ends with . or ! or ?
    # so simply count these characters
            sentences += line.count('.') + line.count('!') + line.count('?')
    # create a list of words
    # use None to split at any whitespace regardless of length
    # so for instance double space counts as one space
     #Average word lenght
average_chars = num_chars/num_words
        
    #Average sentence lenght
average_sentence = num_words/sentences

print("Number of words: " + str(num_words))
print("Number of sentences: " + str(sentences))
print("Average characters per word: " + str(average_chars))
print("Average sentence lenght: "+str(average_sentence))