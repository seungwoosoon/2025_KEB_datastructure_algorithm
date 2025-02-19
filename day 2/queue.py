# 큐
# 먼저 들어온걸 먼저 처리
# FiFO
# 프론트 // @@@@@ // 리어
# 인큐: 삽입 // 디큐: 삭제
# 예시) 공용 프린터 => 작업 순서대로 출력됨.
class Node: 
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
class queue:
    
    def __init__(self): # 생성자 메서드
        self.front =None
        self.rear = None
        self._size = 0
        
    def enqueue(self, data): # 삽입
        while len(self.s1) != 0: ##
            self.s2.append(self.s1.pop())
        self.s1.append(data)
        while len(self.s2) != 0:
            self.s1.append(self.s2.pop())
    
    def dequeue(self): # 삭제
        if len(self.s1) == 0:
            raise Exception("Empty queue!")
        return self.s1.pop()
    
    # def size(self) -> int: #사이즈
    #     return self._size
    
if __name__ == "__main__":
    q = queue()
    q.enqueue(7) ##
    q.enqueue(-11)
    q.enqueue(8)
    
    for _ in range(3):
        print(q.dequeue())
    
    
    
## 파이썬 내장된 큐 클래스

# from queue import Queue

# q = Queue()
# q.put('a') # enqueue
# print(q.qsize())
# print(q.get()) # dequeue

# 내장함수 있어서 그냥 이거 쓰면됨.