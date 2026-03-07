n,k=map(int,input().split())
score=list(map(int,input().split()))
cutoff=score[k-1]
count=0
for s in score:
    if s>=cutoff and s>0:
        count+=1
print(count)        