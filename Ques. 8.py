def readingTextFile():
    myFile = open('Ques. 8(Pages.txt)', 'r')
    url = []
    while True:
        line = myFile.readline()
        if not line:
            break
        wordList = line.rstrip("\n").split(',')
        wordList[2]=wordList[2].replace("This has reference to","").strip()
        url.append(wordList)
    return url

def cal_Importance(url, n):
    newImp = 0.0
    count = 0
    updDict = {}
    for val in url:
        for j in range(2,len(val)):
            for i in range(len(url)):
                if url[i][0] == val[j]:
                    newImp += float(url[i][1])
                    count+=1
        updDict[val[0]] = round((newImp/count),2) 
        newImp = 0.0
        count = 0
    
    for i in range(n):
        max_Key = next(iter(updDict))
        for key in updDict:
            if updDict[key] > updDict[max_Key]:
                max_Key = key
        print(max_Key)
        del updDict[max_Key]
        
n = int(input("Enter the value of n:- "))
url = readingTextFile()
cal_Importance(url, n)