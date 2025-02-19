def is_even(n) -> bool:
    # 요런식으로 만들거 적어주는게 필요한가봄
    """
    짝수 판정 함수
    :parm n: 판정할 정수
    :return: 짝수면 True, 홀수면 False
    """
#    if n % 2 ==0:
#        return True
#    return False

    # 비트 연산자만 이용해서 홀짝 판별
    # 1011 & 0001 => 맨뒤 4번쨰 자리 1을 이용해서 1 있으면 홀수, 없으면 짝수.
    return not n & 1 # 비트연사자 이용해서 한줄로 홀짝 판별.


n = int(input())
print(is_even(n))

