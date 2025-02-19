# 스택 만들기

# => 가장 많이 사용되는 자료구조 중 하나 
# => 너비 우선 탐색 알고리즘.
# => 우리 맨날 쓰는 ctrl + z => 이것도 스택 사용 예제임. => 마지막으로 쓴거 꺼내고 넣기.
# => 웹브라우저 뒤로가기 앞으로가기 => 스택 두개 써서 만듬.
# FILO
# Push: 삽입 // Pop: 추출.

class Stack: #스택 생성.
    def __init__(self): # 리스트 만들기
        self.items = list() # 생성자 메서드.
        
    def push(self, data): # 위에서부터 밀어 넣기.
        self.items.append(data)
        
    def pop(self): # 위에서부터 사출
        return self.items.pop()

    def size(self): # 사이즈 
        return len(self.items)
    
    def peek(self) -> object: # object 얘는 뭘 넣을지 모를때 넣는 NULL 같은 거임.
        return self.items[-1] # peek => 요소 사출 안하고 보기 용도.
    
    def is_empty(self) -> bool: # 빈지 확인
        return len(self.items) == 0 # 스택 크기가 0 이면 비어있다고 true 출력.

s1 = Stack()
s1.push(-9)
s1.push(11)
s1.push(123)

print(s1.pop()) # 이거는 아예 마지막 값이 사출됨.
print(s1.peek()) #마지막으로 들어간게 출력.
print(s1.peek())

print(s1.size())
print(s1.pop())
print(s1.pop())

print(s1.size())
print(s1.is_empty()) 
