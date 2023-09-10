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
n,k=map(int,input().split())

result=n//k+n%k

print(result)