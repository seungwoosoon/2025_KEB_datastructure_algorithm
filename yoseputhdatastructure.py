from collections import deque
n, k = map(int, input().split()) 
queue = deque([])
for i in range(1,n+1):
    queue.append(i)
print("<",end="")
while queue:
    queue.rotate(-k+1)
    if len(queue) != 1:
        print(queue.popleft(),end=", ")
    else:
        print(queue.popleft(),end=">")