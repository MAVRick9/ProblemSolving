n,m,k=map(int,input().split())

data=list(map(int,input().split()))
data.sort()

first=data[n-1]
second=data[n-2]
result=0


result=first*(int(m/(k+1))*k+m%(k+1))+second*(int(m/(k+1)))

print(result)

# count=int(m/(k+1))*k
# count+=m%(k+1)
# result+=(count)*first
# result+=(m-count)*second