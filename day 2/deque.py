# deque => 효율이 좋다.

from collections import deque

d = deque()
d.append(7)
d.append(-11)
d.append(8)

if __name__ == "__main__":
    for data in d:
        print(data)