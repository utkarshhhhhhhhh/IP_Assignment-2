def course(s):
    alphabets = ""
    if len(s)!=6 or not(s[0].isalnum()) or not(s[0].isupper()) or not(s[5].isdigit()) or not(s.isupper()):
        return False
    for val in s:
            if val.isalpha():
                alphabets += val 
    if s.replace(alphabets,"") == s:
        return False
        
    return True

def cred(n):
    if n in [1,2,4]:
        return True
    return False

def gra(s):
    l1=["A+","A","A-","B","B-","C","C-","D","F"]
    if s in l1:
        return True
    return False
def Course_Number(Input):
    for i in range(len(Input)):
        if len(Input[i][0])==6 and Input[i][0].isalnum() and Input[i][0].isupper() and Input[i][0][0].isupper() and Input[i][0][5].isdigit():
            return Input[i][0]
        else:
            return False
            
def Credits(Input):
    l=[1,2,4]
    Total_Credits=0
    for i in range(len(Input)):
        if int(Input[i][1]) in l:
            Total_Credits += int(Input[i][1])
        else:
            print("Incorrect Credit")
    return(Total_Credits)
        
def Grade(Input):
    l1=["A+","A","A-","B","B-","C","C-","D","F"]
    l2=[10,10,9,8,7,6,5,4,2]
    marks=[]
    for i in range(len(Input)):
        if Input[i][2] in l1:
            index=l1.index(Input[i][2])
            marks.append(l2[index])
        else:
            print("Incorrect Grade")
    return marks
        
def SGPA(Input):
    while True:
        sgpa = 0
        for i in range(len(Input)):
            sgpa += int(Input[i][1])*Grade(Input)[i]
        return round(sgpa/Credits(Input),2)
    
Input=[]
while True:
    lst=list(map(str, input().split()))
    if lst!=[]:
        if course(lst[0]) and cred(int(lst[1])) and gra(lst[2]):
            Input.append(lst)
        else:
            if not(course(lst[0])):
                print("Incorrect Course Name")
            if not(cred(int(lst[1]))):
                print("Incorrect Credits")
            if not(gra(lst[2])):
                print("Incorrect Grade")
    else:
        break
Course_Number(Input)
print("_______________________")
print("     Transcript")
print("_______________________")

for i in range(len(Input)):
    print(Input[i][0],":",Grade(Input)[i])
print("_______________________")
print("SGPA:",format(SGPA(Input),".2f"))
print("_______________________")
print("                ")