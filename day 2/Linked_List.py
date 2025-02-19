# 링크드 리스트.

# => 요소를 삽입해도 다른 데이터들을 밀어낼 필요가 없음.
# 양방향 연결 => 이중 연결 리스트.
# 처음과 끝을 이어서 => 원형 리스트
# => 삽입 삭제에 강점이 있다.

import random
# 노드 클래스
class Node: 
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

# 링크 클래스
class LinkedList:
    def __init__(self): # 생성자 메서드
        self.head = None
    
    def append(self, data):
        if not self.head:
            self.head = Node(data)
            return

        current = self.head
        while current.next: # if node exist
            current = current.next
        current.next = Node(data)
        
        def __str__(self):
            node = self.head
            while node != None:
                print(node.data)
                node = node.next
            return "end"

    def search(self, target):
        current = self.head
        while current.next:
            if current.data == target: # 찾으면 True
                return True
            else:
                current = current.next
        return False # 못찾으면 False => 원하는게 없다.

if __name__ == "__main__":
    l = LinkedList()
    
    i = 0
    while i < 20:
        n=random.randint(1,20)
        l.append(n)
        print(n, end= ' ')
        i = i+1
        
    #print(l)
    print(l.search(10))

    #print(l) # => 저거 객체 출력하면 <__main__.LinkedList object at 0x102983fd0> 이렇게 나옴.


    