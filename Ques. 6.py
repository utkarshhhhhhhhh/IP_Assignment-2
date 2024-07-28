def Grade_Evaluation(n):
    Grades=['A','A-','B','B-','C','C-','D','F']
    if 100>=n>80:
        return Grades[0]
    elif 80>=n>70:
        return Grades[1]
    elif 70>=n>60:
        return Grades[2]
    elif 70>=n>60:
        return Grades[3]
    elif 60>=n>50:
        return Grades[4]
    elif 50>=n>40:
        return Grades[5]
    elif 40>=n>30:
        return Grades[6]
    elif 30>=n>=0:
        return Grades[7]

weights = [(10, 5), (10, 5), (40, 20), (100, 30), (10,5), (10,5), (80,30)]
f1=open("Ques. 6(IP_Marks.txt)","r")
f2=open("Ques. 6(IP_Grades.txt)","w")

L=f1.read().splitlines()
for i in L:
    a=i.split(",")
    for j in range(1,len(a)):
        a[j]=int(a[j])
    f2.write(a[0]+", ")
    marks=0
    for i in range(1,len(a)):
        marks+=(a[i]*weights[i-1][1])/(weights[i-1][0])
    marks=int(marks)
    f2.write(str(marks))
    f2.write(", ")
    f2.write(Grade_Evaluation(marks))
    f2.write("\n")
f2.close()
f1.close()