from typing import Counter


a = int(input())

for i in range(a):
    countv=0
    countc=0
    b=list(input())
    R=len(b)
    for j in range(R):
        for l in b[j]:
            for m in range(R):
                if(l==b[m]):
                    dict({})
        c=['A','E','I','O','U']
        for k in c:
            if(k==b[j]):
                countv+=1
    countc=R-countv
    print(countc,countv)
