import sys
sys.stdin=open("input.txt","r")

def Count(capacity):       #dvd몇장 필요한지 return
    cnt=1       #dvd 1장은 필요
    sum=0       #dvd에 저장되는 노래들 sum
    for x in Music:
        if sum+x>capacity:      #용량 초과
            cnt+=1
            sum=x
        else:       #저장 가능
            sum+=x
    return cnt

n, m=map(int, input().split())      #n:곡의 수, m:dvd개수
Music=list(map(int, input().split()))
lt=1
rt=sum(Music)
res=0 
while lt<=rt:    #이분 검색
    mid=(lt+rt)//2
    if Count(mid)<=m:
        res=mid
        rt=mid-1 #더 좋은 답을 위해서..
    else:
        lt=mid+1    
print(res)