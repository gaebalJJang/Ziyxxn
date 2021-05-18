import sys
sys.stdin=open("input.txt","r")

def Count(len):     
    cnt=0
    for x in Line:
        cnt+=(x//len)
    return cnt      #그 길이로 만들수 있는 랜선의 개수

k, n=map(int, input().split())
Line=[]     #empty list
res=0
largest=0   #가장 긴 랜선
for i in range(k):
    tmp=int(input())
    Line.append(tmp)
    largest=max(largest, tmp)
lt=1
rt=largest
while lt<rt:    #이분 검색
    mid=(lt+rt)//2
    if Count(mid)>=n:
        res=mid
        lt=mid+1 #더 좋은 답을 위해서..
    else:
        rt=mid-1    #더 긴쪽을 버려!
print(res)