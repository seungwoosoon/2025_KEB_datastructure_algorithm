# 8진수 변환 함수

def dec_oct(n) -> int: # 재귀함수 이용
    if n==0:
        return ""
    else:
        return dec_oct(n//8) + str(n%8)


n = int(input())
print(n, dec_oct(n))

# ex
# 65 => 8 1 0 => 65 8 1 => 1 0 1
# 재귀함수 사용 => 코드 간결해짐 => 이거 살짝만 바꾸면 2진수 변환으로 바꿀수있음.