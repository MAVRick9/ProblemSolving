# loc =input()
# c={'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8}
# x=c[loc[0]]
# y=int(loc[1])
# count=0
# dx=[2,2,1,1,-1,-1,-2,-2]
# dy=[-1,1,-2,2,-2,2,-1,1]
#
# for i in range(8):
#     if(dx[i]+x>8 or dx[i]+x<1 or dy[i]+y>8 or dy[i]+y<1):
#
#         continue
#     print(dx[i]+x, dy[i]+y)
#     count+=1
#
# print(count)

loc=input()
c=int(ord(loc[0]))-int(ord('a'))+1
r=int(loc[1])

steps=[(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]

result=0
for step in steps:
    next_r=step[0] + r
    next_c=step[1]+c
    if(next_r>=1 and next_r<=8 and next_c>=1 and next_c<=8):
        result+=1
print(result)