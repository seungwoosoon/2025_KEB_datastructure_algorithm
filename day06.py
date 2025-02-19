import time
# import numpy as np
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
    
factmemo = {}
def fact(n) -> int:
    if n in factmemo:
        return factmemo[n]
    elif n <= 1:
        return n
    else:
        factmemo[n] = fact(n-1) * n
        return factmemo[n]

# n = int(input())
# print(is_even(n))
# print(eightjinsu(65))
# print(fibo(5))
# print(fact(10))
# print(memo)

import random
ran = [1,100]
def guessnum(f,l):
    # return random.randint(f,l)
    return int((f+l)/2)

answer = random.randint(1, 100)
chance = 7

with open('guess.txt','w') as fp:
    while chance != 0:
        guess = guessnum(ran[0],ran[1])
        if guess == answer:
            print(f'You win. Answer is {answer}')
            fp.write(f"{answer}정답 \n")
            break
        elif guess > answer:
            chance = chance - 1
            print(f'{guess} is bigger. Chance left : {chance}')
            fp.write(f"{guess} 커요 \n")
            ran[1] = guess-1
        else:
            chance = chance - 1
            print(f'{guess} is lower. Chance left : {chance}')
            fp.write(f"{guess} 작아요 \n")
            ran[0] = guess +1
    else:
        print(f'You lost. Answer is {answer}')
        fp.write("실패~~~~ \n")
