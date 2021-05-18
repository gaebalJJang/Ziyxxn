import sys         
sys.stdin=open("input.txt","r")
n=int(input())
meeting=[]
for i in range(n):
    s, e=map(int, input().split())    #s:start, e:end
    meeting.append((s, e))
meeting.sort(key=lambda x : (x[1], x[0]))       #meeting이라는 자료형에서 하나 받고 x의 1번이 우선순위 0번이 차순 == 정렬 순위 바꾸기

et=0        #endTime
cnt=0
for s, e in meeting:
    if s>=et:
        et=e
        cnt+=1
print(cnt)
