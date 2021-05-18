import sys    
from collections import deque      
sys.stdin=open("input.txt","r")
n, limit=map(int, input().split())
p=list(map(int, input().split()))
p.sort()
p=deque(p)      #p리스트가 deque 자료구조로 변경
cnt=0
while p:
    if len(p)==1:       #마지막 1명 보트타고 가면됨
        cnt==1
        break
    if p[0]+p[-1]>limit:
        p.pop()
        cnt+=1
    else:
       #p.pop(0)        #맨 앞자리 pop하면 뒤의 자료들이 앞으로 땡겨짐 ==> 비효율적 따라서 deque사용
        p.popleft()     #조금더 효율적으로 deque에서 사용
        p.pop()
        cnt+=1
print(cnt)
