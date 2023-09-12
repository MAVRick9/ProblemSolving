# n,m 입력받기
n,m=map(int,(input().split()))
#현재 캐릭터 x,y좌표 방향 입력받기
cA, cB, dir=map(int,(input().split()))

#맵 정보 입력받기
mp=[]
for i in range(n):
    mp.append(list(map(int,input().split())))

#방향 이동 순서대로 북 동 남 서
dx=[-1,0,1,0]
dy=[0,1,0,-1]

# 가본 장소 체크
flag=[[0]*m for _ in range(n)]
# 가본 칸 수 초기화
count=1
fl=0

flag[cA][cB]=1

while True:
    # 왼쪽 반시계로 회전
    dir-=1
    if(dir<0):
        dir = 3
    # 가보지 않은 칸이고 바다가 아니면 전진
    if(flag[cA+dx[dir]][cB+dy[dir]]==0 and mp[cA+dx[dir]][cB+dy[dir]]!=1):
        cA+=dx[dir]
        cB+=dy[dir]
        flag[cA][cB] = 1
        fl=0
        count+=1
    else:
        fl+=1
    # 동서남북 모두 가본 칸이거나 바다로 된 칸이면 한 칸 후진
    if (fl == 4):
        if (mp[cA - dx[dir]][cB - dy[dir]] == 0):
            cA -= dx[dir]
            cB -= dy[dir]

        else:
            break

        fl=0



print(count)







