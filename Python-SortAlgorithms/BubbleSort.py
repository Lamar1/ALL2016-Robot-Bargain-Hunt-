"""
Bubble sort algorithm 
"""

def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

alist = ["E","A", "B", "C", "D", "F"]
bubbleSort(alist)
print(alist)
