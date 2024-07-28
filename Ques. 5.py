n=int(input("Enter The Value Of N:"))
m=[]
for i in range(n):
    l=[]
    l=list(map(int,input().split()))
    l.append(1)
    m.append(l)
    
Result_1=[]
for i in range(n):
    l=[]
    for j in range(n+1):
        l.append(0)
    Result_1.append(l)
Cx=int(input("Enter The Value Of Cx:"))
Cy=int(input("Enter The Value Of Cy:"))
Scaling_List=[[Cx,0,0],[0,Cy,0],[0,0,1]]

for i in range(len(m)):
    for j in range(len(Scaling_List[0])):
        for k in range(len(Scaling_List)):
            Result_1[i][j] += m[i][k] * Scaling_List[j][k]
Result=[]
for i in range(len(Result_1)):
    Result_2=[]
    Result_2.append(Result_1[i][0]) 
    Result_2.append(Result_1[i][1]) 
    Result.append(Result_2)

print(Result)