#Algorithm for sorting a list of words into alphabetical order using bubble sort.

def bubbleSort(wordList):
    for i in range(len(wordList) - 1):
        for j in range(len(wordList) - 1):
            
            if (wordList[j])[0] > (wordList[j+1])[0]:
                wordList[j], wordList[j+1] = wordList[j+1], wordList[j]
    return wordList

import random
import string
list1 = [random.choice(string.ascii_uppercase) for i in range(10)]
print ("Before: ", list1)
print ("After:  ", bubbleSort(list1))
