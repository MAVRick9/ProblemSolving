# n입력받기
n=int(input())
# 이동 경로 입력받기
route=input().split()

move_type=['U', 'D', 'L', 'R']
dx=[-1,1,0,0]
dy=[0,0,-1,1]
x, y= 1, 1
for r in route:
    for i in range(len(move_type)):
        if(r==move_type[i]):
            x+=dx[i]
            y+=dy[i]
        if(x<1 or y<1 or x>n or y>n):
            x-=dx[i]
            y-=dy[i]

print(x,y)


# if(r==move_type[i]):
#             nx+=dx[i]
#             ny+=dy[i]
#         if(x<1 or y<1 or x>n or y>n):
#             continue
#         x,y=nx,ny