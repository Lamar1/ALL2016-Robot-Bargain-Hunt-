#Python implementation of the QuickSort Algorithm

def quickSort(wordList):
    lessThan = []
    equalTo = []
    greaterThan = []
    if len(wordList) > 1:
        pivot = wordList[0]
        for i in range(len(wordList)):
            if wordList[i] < pivot:
                lessThan.append(wordList[i])
            elif wordList[i] > pivot:
                greaterThan.append(wordList[i])
            else:
                equalTo.append(wordList[i])
        return quickSort(lessThan) + equalTo + quickSort(greaterThan)
    else:
        return wordList

import random
import string
list1 = [random.choice(string.ascii_uppercase) for i in range(10)]
print ("Before: ", list1)
print ("After:  ", quickSort(list1))
