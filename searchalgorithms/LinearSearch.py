"""
Linear seach algorithm
"""

__author__ = "Ryan"

def linearSearch (myItem):
    foundItem = False
    pos = 0
    while pos < len(_List4Table) and not foundItem:
        if myList[pos] == myItem:
            foundItem = True
            pos = pos + 1
        return foundItem

theList = ["apple", "banana", "orange"]
theItem = "apple"
isFound = linearSearch(theItem)
if isFound:
    print ("Found")
else:
    print ("Not found")
