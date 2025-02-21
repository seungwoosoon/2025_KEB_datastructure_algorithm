n = int(input())  
k = int(input())  
arr = list(range(1, n + 1))  # 1부터 n까지 리스트 생성  

idx = k - 1  # 인덱스는 0부터 시작하므로 k-1로 조정

while arr:
    idx %= len(arr)  # 인덱스가 리스트 길이를 초과하지 않도록 조정
    print(arr[idx], end="")  # 출력
    arr.pop(idx)  # 해당 요소 삭제

    if arr:  # 리스트가 비어있지 않으면
        idx = (idx + k - 1) % len(arr)  # 다음 k 번째 인덱스 계산