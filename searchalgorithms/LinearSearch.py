"""
Linear seach algorithm
"""

__author__ = "Ryan"

def linearSearch (myItem, myList):
    foundItem = False
    pos = 0
    while pos < len(myList) and not foundItem:
        if myList[pos] == myItem:
            foundItem = True
            pos = pos + 1
        return foundItem

theList = ["apple", "banana", "orange"]
theItem = "apple"
isFound = linearSearch(theItem, theList)
if isFound:
    print ("Found")
else:
    print ("Not found")
