#N,M,K를 공백으로 구분하여 입력받기
n,m,k=map(int, input().split())
#N개의 수를 공백으로 구분하여 입력받기
data=list(map(int, input().split()))

data.sort() #입력받은 수들 정렬
first=data[n-1] #가장 큰 수
second=data[n-2]

result=0

while True:
    for i in range(k): #가장 큰 수 K번 더하기
        if m==0: #m==0이면 반복문 탈출
            break
        result+=first
        m-=1 #더할 때마다 1씩 빼기
    if m==0: #m==0이면 반복문 탈출
        break
    result+=second
    m-=1

print(result)


