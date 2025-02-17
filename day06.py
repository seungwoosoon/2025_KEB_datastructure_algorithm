def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)

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

# n = int(input())
# print(is_even(n))
print(eightjinsu(65))