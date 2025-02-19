# 공간복잡도 예제

memo = dict() # 리스트 써도됨
def fibo(n) -> int:
    if n in memo: # 딕셔너리에 이미 계산된 결과가 있으면 그 값을 리턴.
        return memo[n]
    elif n<=1:
        return n
    else: 
        memo[n] = fibo(n-2) + fibo(n-1) #딕셔너리에 계산된 결과값이 없을 경우 => 딕셔너리에 추가.
        return memo[n]

# 원리 => 이미 계산된 거 있으면 계산 안함. 
print(fibo(5))
print(memo)
