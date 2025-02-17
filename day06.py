import time
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} 실행 시간: {end - start:.9f}초")
        return result
    return wrapper

def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)

@timer
def eightjinsu(n):
    if n == 0:
        return ""
    return eightjinsu(n//8) + str(n%8)



def is_even(n) -> bool:
    """
    짝수 판정 함수
    :param n: 판정할 정수
    :return: 짝수면 True, 홀수면 False
    """
    return not bool(n&1)

memo = dict()
def fibo(n) -> int:
    if n in memo:
        return memo[n]
    elif n<=1:
        return n
    else:
        memo[n] = fibo(n-2) + fibo(n-1)
        return memo[n]

# n = int(input())
# print(is_even(n))
# print(eightjinsu(65))
print(fibo(5))
print(memo)