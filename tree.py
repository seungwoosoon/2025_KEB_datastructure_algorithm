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



node1=treenode()
node1.value = "화사"

node2=treenode()
node2.value = "솔라"
node1.left = node2

node3=treenode()
node3.value = "휘인"
node2.left = node3

node4=treenode()
node4.value = "쯔위"
node2.right = node4

node5=treenode()
node5.value = "문별"
node1.right = node5

node6=treenode()
node6.value = "선미"
node5.left = node6
