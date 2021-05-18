import sys    
from collections import deque      
sys.stdin=open("input.txt","r")
n=int(input())
a=list(map(int, input().split()))
seq=[0]*n
for i in range(n):      #i가 정렬된 자료 처리
    for j in range(n): 
        if a[i]==0 and seq[j]==0:       # ***중요!!!  자기 앞의 빈 공간 확보했다 and 뒤에도 빈공간이다
            seq[j]=i+1
            break
        elif seq[j]==0:     #빈자리 발견되면
            a[i]-=1
for x in seq:
    print(x, end=' ')