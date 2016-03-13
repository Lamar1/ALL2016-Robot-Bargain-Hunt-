class SortAlgorithms:

    def bubbleSort(wordList):
    #Function to sort a list into alphabetical/numerical order using Bubble Sort algorithm
        for i in range(len(wordList) - 1):
            for j in range(len(wordList) - 1):
                if (wordList[j])[0] > (wordList[j+1])[0]:
                    wordList[j], wordList[j+1] = wordList[j+1], wordList[j]
        return wordList

    def bubbleSortReverse(wordList):
    #Function to sort a list into reverse alphabetical/numerical order using Bubble Sort algorithm
        for i in range(len(wordList) - 1):
            for j in range(len(wordList) - 1):
                if (wordList[j])[0] < (wordList[j+1])[0]:
                    wordList[j], wordList[j+1] = wordList[j+1], wordList[j]
        return wordList


    def insertionSort(wordList):
    #Function to sort a list into alphabetical/numerical order using Insertion Sort algorithm
        for i in range(len(wordList)):
            comparisonValue = wordList[i]
            while (i > 0) and (wordList[i-1] > comparisonValue):
                wordList[i] = wordList[i-1]
                i -= 1
            wordList[i] = comparisonValue
        return wordList

    def insertionSortReverse(wordList):
    #Function to sort a list into reverse alphabetical/numerical order using Insertion Sort algorithm
        for i in range(len(wordList)):
            comparisonValue = wordList[i]
            while (i > 0) and (wordList[i-1] < comparisonValue):
                wordList[i] = wordList[i-1]
                i -= 1
            wordList[i] = comparisonValue
        return wordList


    def quickSort(wordList):
    #Function to sort a list into alphabetical/numerical order using Quick Sort algorithm
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

    def quickSortReverse(wordList):
    #Function to sort a list into  reverse alphabetical/numerical order using Quick Sort algorithm
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
            return quickSortReverse(greaterThan) + equalTo + quickSortReverse(lessThan)
        else:
            return wordList

import random
import string
exampleList = [random.choice(string.ascii_uppercase) for i in range(10)]
print(SortAlgorithms.bubbleSortReverse(exampleList))
