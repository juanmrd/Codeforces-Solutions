n = int(input())
s = 0
for i in range(n):
  v,c = map(int, input().split())
  if v+1 < c:
    s += 1
print(s) 
