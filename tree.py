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

def deligin(root,did):
    current = root
    parent = None
    while True:
        if current.value == did:
            if current.left == None and current.right == None:
                del(current)
                break
            elif current.left != None and current.right == None:
                parent.left = current.left
                del(current)
                break
            elif current.left == None and current.right != None:
                parent.left = current.right
                del(current)
                break
            elif current.left != None and current.right != None:
                parent.left = current.right
                current.right.left = current.left
                del(current)
                break
        elif current.value <did:
            if current.right is None:
                print("없다")
                break
            parent = current
            current = current.right
        elif did < current.value:
            if current.left is None:
                print("없다")
                break
            parent = current
            current = current.left

if __name__ == "__main__":
    groups = ['블랙핑크','레드벨벳','마마무','에이핑크','걸스데이','트와이스']
    node = treenode()
    node.value=groups[0]
    root = node

    for group in groups[1:]:
        node = treenode()
        node.value = group
        current = root
        while True:
            if group < current.value:
                if current.left is None:
                    current.left = node
                    break
                current = current.left
            elif group > current.value:
                if current.right is None:
                    current.right = node
                    break
                current = current.right
        
    findigin(root,'핑클')
    deligin(root,'에이핑크')

