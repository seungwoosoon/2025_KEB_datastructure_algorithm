def a(i):
    j = 9
    print(i,j)

def b(k):
    a(1)
    print(k)

def main():
    print("start")
    b(3)

if __name__ == "__main__":
    main()
    
# 디버깅 연습 => 중단점 찍고 할것.