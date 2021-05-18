import sys         
sys.stdin=open("input.txt","r")
def Count(len):
    cnt=1       #말 한마리를 배치
    ep=Line[0]  #첫번째 말 배치 지점
    for i in range(1, n):
        if Line[i]-ep>=len:  
            cnt+=1
            ep=Line[i]
    return cnt

n, c=map(int, input().split())   
Line=[]
for _ in range(n):
    tmp=int(input())
    Line.append(tmp)
Line.sort()
lt=1
rt=Line[n-1]
res=0 
while lt<=rt:    #이분 검색
    mid=(lt+rt)//2
    if Count(mid)>=c:
        res=mid
        lt=mid+1 #더 좋은 답을 위해서..
    else:
        rt=mid-1    
print(res)