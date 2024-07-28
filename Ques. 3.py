def readingTextFile():
    signDict = {}
    count = 0
    myFile = open('Ques. 3(Signature.txt)', 'r')
    while True:
        line = myFile.readline()
        if not line:
            break
        wordList = line.split(',')
        if len(wordList)>1:
            if int(wordList[1]) > 0:
                count = count + 1
        else:
            name = wordList[0]
            count = 0
        signDict[name] = count
    findMaxValue(signDict)

def findMaxValue(totalSignDict):
    # Initialize max_key to the first key in the dictionary
    max_Name = next(iter(totalSignDict))
    min_Name = next(iter(totalSignDict))
    # Iterate over the keys in the dictionary
    for key in totalSignDict:
        if totalSignDict[key] > totalSignDict[max_Name]:
            max_Name = key
        if totalSignDict[key] < totalSignDict[min_Name]:
            min_Name = key

    if totalSignDict[max_Name] >= 1:
        print(max_Name," gets maximum signs and gets a total of",totalSignDict[max_Name],"signs!!!")
    if totalSignDict[min_Name] >= 1:
        print(min_Name," gets minimum signs and gets a total of",totalSignDict[min_Name],"signs!!!")

readingTextFile()