from collections import deque
class treenode():
     def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right   

def preorder(root):
    if root == None:
        return
    print(root.value,end=" - ")
    preorder(root.left)
    preorder(root.right)

def inorder(root):
    if root == None:
        return
    inorder(root.left)
    print(root.value,end=" - ")
    inorder(root.right)


def postorder(root):
    if root == None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.value,end=" - ")



# node1=treenode()
# node1.value = "화사"

# node2=treenode()
# node2.value = "솔라"
# node1.left = node2

# node3=treenode()
# node3.value = "휘인"
# node2.left = node3

# node4=treenode()
# node4.value = "쯔위"
# node2.right = node4

# node5=treenode()
# node5.value = "문별"
# node1.right = node5

# node6=treenode()
# node6.value = "선미"
# node5.left = node6

def findigin(root,fid):
    current = root
    while True:
        if current.value is fid:
            print(fid, " 찾앗다")
            break
        elif fid < current.value:
            if current.left is None:
                print("없다")
                break
            current = current.left
        else:
            if current.right is None:
                print("없다")
                break
            current = current.right
def deligin(root, key):
    # 기저 조건: 아무 노드도 없으면 그냥 None 반환
    if root is None:
        return None

    # 삭제할 노드를 찾기 위한 재귀 탐색
    if key < root.value:
        root.left = deligin(root.left, key)
    elif key > root.value:
        root.right = deligin(root.right, key)
    else:
        # 삭제할 노드를 찾은 경우 (root.value == key)

        # Case 1: 자식이 없는 경우
        if root.left is None and root.right is None:
            return None

        # Case 2: 한쪽 자식만 있는 경우
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left

        # Case 3: 두 자식이 모두 있는 경우
        # Inorder successor(오른쪽 서브트리의 가장 왼쪽 노드)를 찾는다.
        successor = root.right
        while successor.left:
            successor = successor.left
        
        # 현재 노드의 값을 successor의 값으로 교체
        root.value = successor.value

        # 오른쪽 서브트리에서 successor 노드를 삭제
        root.right = deligin(root.right, successor.value)
    
    return root

def isertnode(root,value):
    current = root
    node = treenode()
    node.value = value
    while True:
        if value < current.value:
            if current.left is None:
                current.left = node
                break
            current = current.left
        elif value > current.value:
            if current.right is None:
                current.right = node
                break
            current = current.right
        else:
            break

def cntlentree(root):
    if root is None:
        return 0
    return 1+cntlentree(root.left)+cntlentree(root.right)

def bfs(node):
    if node is None:
        return

    queue = deque([node])
    while queue:
        current = queue.popleft()
        print(f"{current.value}", end=' ')
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

if __name__ == "__main__":
    groups = ['블랙핑크','레드벨벳','마마무','에이핑크','걸스데이','트와이스']
    node = treenode()
    node.value=groups[0]
    root = node

    for group in groups[1:]:
        isertnode(root,group)
        
    findigin(root,'핑클')
    preorder(root)
    deligin(root,'에이핑크')
    print()
    preorder(root)
    print()
    bfs(root)

