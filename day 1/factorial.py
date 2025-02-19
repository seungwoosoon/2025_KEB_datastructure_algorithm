# 재귀 연습.

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1) # 재귀함수 => 직관성이 젤 중요
n = int(input())

print(factorial(n))
