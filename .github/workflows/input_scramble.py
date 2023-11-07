from collections import OrderedDict
import os
import math


def sortAlphabetically(filename):
    characters = {}
    with open(filename, "r") as f1:
        text = f1.read()
    for i in text:
        if i in characters.keys():
            characters[i] += 1
        else:
            characters[i] = 1
    myChars = list(characters.keys())
    myChars.sort()
    sortedCharacters = OrderedDict()
    for i in myChars:
        sortedCharacters[i] = characters[i]

    numOfColumns = len(sortedCharacters)
    numOfRows = math.ceil(os.stat(filename).st_size / numOfColumns)
    print(numOfRows)
    for i in myChars:
        if sortedCharacters[i] >= numOfRows:
            sortedCharacters[i] = sortedCharacters[i] % numOfRows
    key = list(sortedCharacters.values())
    with open(filename, "r") as f1:
        finalmat = []
        string = ""
        for i in range(numOfRows):
            tempmat = []
            for j in range(numOfColumns):
                string = f1.read(1)
                if string == "":
                    string = "@"
                tempmat.append(string)
            finalmat.append(tempmat)
        for i in finalmat:
            print(i)
        print("key :", key)
        finalString = ""
        for i in range(numOfColumns):
            for j in range(key[i], key[i] + numOfRows):
                finalString += finalmat[j % numOfRows][i]
        print(finalString)


sortAlphabetically("file1.txt")

