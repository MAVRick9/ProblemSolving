# n,k 입력받기
# n,k=map(int,input().split())
#
# result=0
#
# while (n!=1):
#     if(n%k==0):
#         n=n//k
#         result+=1
#     else:
#         n-=1
#         result+=1
#
# print(result)

# n,k 입력받기
n, k=map(int, input().split())

result=0

while True:
    #n이 k의 배수가 될 때까지 1씩 빼기
    target=(n//k)*k
    result+=(n-target)
    n=target
    # n이 k보다 작으면 반복문 탈출
    if n<k:
        break
    # k로 나누기
    result += 1
    n//=k


# 마지막으로 남은 수에 1씩 빼기
result+=(n-1)

print(result)