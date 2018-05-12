# Modules
import os

# Set file path
txtpath = os.path.join("paragraph_1.txt")

# Set all variables to default
num_words = 0
lines = 0
sentences = 0
num_chars = 0
blanklines = 0

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

txtpath1 = os.path.join("paragraph_2.txt")
num_words1 = 0
lines1 = 0
sentences1 = 0
num_chars1 = 0
blanklines1 = 0

with open(txtpath1) as paragraph:
   #Find out word count
   #print (paragraph.read())
   for line in paragraph:
       words = line.split()
       num_words1 += len(words)
       num_chars1 += len(line)
        
       lines1 += 1
       if line.startswith('\n'):   
            blanklines1 += 1
       else:
    # assume that each sentence ends with . or ! or ?
    # so simply count these characters
            sentences1 += line.count('.') + line.count('!') + line.count('?')
    # create a list of words
    # use None to split at any whitespace regardless of length
    # so for instance double space counts as one space
     #Average word lenght
average_chars1 = num_chars1/num_words1
        
    #Average sentence lenght
average_sentence1 = num_words1/sentences1

print("Number of words: " + str(num_words1))
print("Number of sentences: " + str(sentences1))
print("Average characters per word: " + str(average_chars1))
print("Average sentence lenght: "+str(average_sentence1)+"\n") 


print("Number of words: " + str(num_words))
print("Number of sentences: " + str(sentences))
print("Average characters per word: " + str(average_chars))
print("Average sentence lenght: "+str(average_sentence))

