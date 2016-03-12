"""
Linear seach algorithm
"""

def linear(item):
    locatedItem = False
    pos = 0
    while pos < len(_List4Table) and not locatedItem:
        if myList[pos] == item:
            locatedItem = True
            pos = pos + 1
        return locatedItem

itemList = ["Caviar", "Coconut", "Grapes". "Potatoes", "Apple Butter", "Clams"]
item = "Grapes"
isFound = linear(item)
if isFound:
    print ("Item is in our store.")
else:
    print ("This item is not in our store.")
