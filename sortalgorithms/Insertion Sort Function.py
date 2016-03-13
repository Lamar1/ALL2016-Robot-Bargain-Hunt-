#Algorithm for sorting a list of words into alphabetical order using insertion sort.

def insertionSort(wordList):
    for i in range(len(wordList)):
        comparisonValue = wordList[i]
        while (i > 0) and (wordList[i-1] > comparisonValue):
            wordList[i] = wordList[i-1]
            i -= 1
        wordList[i] = comparisonValue
    return wordList

import random
import string
exampleList = [random.choice(string.ascii_uppercase) for i in range(10)]
print ("Before: ", exampleList)
print ("After:  ", insertionSort(exampleList))
