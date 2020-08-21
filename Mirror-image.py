a=int(input())
result=[]
square1=[]
for i in range(a):
    string=''
    Row_Column=list(map(int,input().split()))
    for j in range(Row_Column[0]):
        spl=input()
        string=string+(spl)
    string=string[::-1]
    result.append(list(string))
    square1.append(Row_Column[1])
s=0
count1=0
count2=0
square2=0
t=1
for k in result:
    print('Test',t)
    for n in k:
        solution=""
        while(s<=len(k)-1):
            solution=solution+k[s]
            count1=count1+1
            count2=count2+1
            s=s+1
            if(count1==square1[square2]):
                count1=0
                break
        print(solution)
        if(count2==len(k)):
            s=0
            square2=square2+1
            count2=0
            t=t+1
            break
