def factorial(number) -> int:

    if number == 1:
        return 1

    res = 1
    for i in range(1,number+1,1):
        res = i*res
    return res

def ncr(n,r) -> int: # 재귀함수 사용해서 반목문과 같은 효과를 누림.
    '''
    조합함수
    :param n:
    :param r
    :return:
    '''
    numerator = factorial(n)
    denominator = factorial(n-r) * factorial(r)
    return numerator / denominator

if __name__ == "__main__":

    n = int(input("input n: "))
    r = int(input("input r: "))

    print(f"{n}C{r} = ", ncr(n,r))
    