class SortAlgorithms:

    def bubbleSort():
    #Function to sort a list into alphabetical/numerical order using Bubble Sort algorithm
        for i in range(len(_List4Table) - 1):
            for j in range(len(_List4Table) - 1):
                if (_List4Table[j])[0] > (_List4Table[j+1])[0]:
                    _List4Table[j], _List4Table[j+1] = _List4Table[j+1], _List4Table[j]
        return _List4Table

    def bubbleSortReverse():
    #Function to sort a list into reverse alphabetical/numerical order using Bubble Sort algorithm
        for i in range(len(_List4Table) - 1):
            for j in range(len(_List4Table) - 1):
                if (_List4Table[j])[0] < (_List4Table[j+1])[0]:
                    _List4Table[j], _List4Table[j+1] = _List4Table[j+1], _List4Table[j]
        return _List4Table


    def insertionSort():
    #Function to sort a list into alphabetical/numerical order using Insertion Sort algorithm
        for i in range(len(_List4Table)):
            comparisonValue = _List4Table[i]
            while (i > 0) and (_List4Table[i-1] > comparisonValue):
                _List4Table[i] = _List4Table[i-1]
                i -= 1
            _List4Table[i] = comparisonValue
        return _List4Table

    def insertionSortReverse():
    #Function to sort a list into reverse alphabetical/numerical order using Insertion Sort algorithm
        for i in range(len(_List4Table)):
            comparisonValue = _List4Table[i]
            while (i > 0) and (_List4Table[i-1] < comparisonValue):
                _List4Table[i] = _List4Table[i-1]
                i -= 1
            _List4Table[i] = comparisonValue
        return _List4Table


    def quickSort():
    #Function to sort a list into alphabetical/numerical order using Quick Sort algorithm
        lessThan = []
        equalTo = []
        greaterThan = []
        if len(_List4Table) > 1:
            pivot = _List4Table[0]
            for i in range(len(_List4Table)):
                if _List4Table[i] < pivot:
                    lessThan.append(_List4Table[i])
                elif _List4Table[i] > pivot:
                    greaterThan.append(_List4Table[i])
                else:
                    equalTo.append(_List4Table[i])
            return quickSort(lessThan) + equalTo + quickSort(greaterThan)
        else:
            return _List4Table

    def quickSortReverse():
    #Function to sort a list into  reverse alphabetical/numerical order using Quick Sort algorithm
        lessThan = []
        equalTo = []
        greaterThan = []
        if len(_List4Table) > 1:
            pivot = _List4Table[0]
            for i in range(len(_List4Table)):
                if _List4Table[i] < pivot:
                    lessThan.append(_List4Table[i])
                elif _List4Table[i] > pivot:
                    greaterThan.append(_List4Table[i])
                else:
                    equalTo.append(_List4Table[i])
            return quickSortReverse(greaterThan) + equalTo + quickSortReverse(lessThan)
        else:
            return _List4Table

import random
import string
exampleList = [random.choice(string.ascii_uppercase) for i in range(10)]
print(SortAlgorithms.bubbleSortReverse(exampleList))
