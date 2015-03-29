# Calculates frequency of words in text files
# User will enter input directory where text files are located.

import os

def word_frequency():
    def word_check(ube):
        return ube[1]


    pathname=input("Enter path to wc_input directory: ")
    listfiles=[file for file in os.listdir(pathname) if file.lower().endswith('.txt')]

    wordz=[]
    numbs=[]
    separated_words=[]
    # Parse through text files in the wc_input directory
    for s in listfiles:
        text=open(os.path.join(pathname,s),'r').read()

        # Extract words from text files and remove characters
        text = text.lower()
        for weird_characters in '!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~':
            text = text.replace(weird_characters, '')
            # Divide separate
        words=text.split()
        separated_words=separated_words + words

        # keep track of words
    counts = {}
    for wordy in separated_words:
        counts[wordy] = counts.get(wordy,0) + 1


    items = list(counts.items())
    items.sort()
    items.sort(key=word_check, reverse=True)
    n=len(items) #number of words to analyse
    for i in range(n):
        word, count = items[i]
        wordz.append(word)
        numbs.append(count)
        # Sort counted words alphabetically
        wordz.sort() 
    # Create output file name and write to output
    enter_output_dir=input("Enter path to wc_output directory: ")
    #newfilename=input("Enter path to wc_output directory and filename: ")
    write_to = open(os.path.join(enter_output_dir,'wc_result.txt'),'w')
    for i,j in zip(wordz,numbs):
        write_to.write("%s\n" % (str(i)+" "+str(j)))

    write_to.close()



