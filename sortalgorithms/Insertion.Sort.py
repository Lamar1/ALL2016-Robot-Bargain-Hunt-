#Algorithm for sorting a list of words into alphabetical order using insertion sort.

def insertionSort(wordList):
    letterOrder = {"A":1, "B":2, "C":3, "D":4, "E":5, "F":6, "G":7, "H":8, "I":9,
               "J":10, "K":11, "L":12, "M":13, "N":14, "O":15, "P":16, "Q":17,
               "R":18, "S":19, "T":20, "U":21, "V":22, "W":23, "X":24, "Y":25,
               "Z":26}
    for i in range(len(wordList)):
        comparisonValue = wordList[i]
        position = i
        while (position > 0) and (wordList[position-1] > comparisonValue):
            wordList[position] = wordList[position-1]
            position -= 1
        wordList[position] = comparisonValue

import random
import string
list1 = [random.choice(string.ascii_uppercase) for i in range(10)]
print ("Before: ", list1)
insertionSort(list1)
print ("After: ", list1)
