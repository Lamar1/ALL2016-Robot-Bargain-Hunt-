#Algorithm for sorting a list of words into alphabetical order using insertion sort.

def insertionSort():
    letterOrder = {"A":1, "B":2, "C":3, "D":4, "E":5, "F":6, "G":7, "H":8, "I":9,
               "J":10, "K":11, "L":12, "M":13, "N":14, "O":15, "P":16, "Q":17,
               "R":18, "S":19, "T":20, "U":21, "V":22, "W":23, "X":24, "Y":25,
               "Z":26}
    for i in range(len(_List4Table)):
        comparisonValue = _List4Table[i]
        position = i
        while (position > 0) and (_List4Table[position-1] > comparisonValue):
            _List4Table[position] = _List4Table[position-1]
            position -= 1
        _List4Table[position] = comparisonValue
