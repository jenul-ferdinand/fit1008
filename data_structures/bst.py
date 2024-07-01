from typing import Callable, TypeVar, Generic

K = TypeVar('K')
I = TypeVar('I')

class TreeNode(Generic[K, I]):
    def __init__(self, key : K, item : I = None) -> None:
        self.key = key
        self.item = item
        self.left = None
        self.right = None
        
    def __str__(self):
        return f'({str(self.key)}, {str(self.item)})'
    
    def get_height(self, node):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return 0
        else:
            l_height = self.get_height(node.left)
            r_height = self.get_height(node.right)

            return max(l_height, r_height) + 1
        
class BinaryTree(Generic[K, I]):
    def __init__(self) -> None:
        self.root = None
        
    def get_height(self) -> int:
        if self.root is None:
            return -1
        
        return self.root.get_height(self.root)
    
if __name__ == '__main__':
    bt = BinaryTree()
    bt.root = TreeNode('A', 'A')
    assert bt.get_height() == 0
    bt.root.left = TreeNode('B', 'B')
    assert bt.get_height() == 1
    bt.root.right = TreeNode('C', 'C')
    assert bt.get_height() == 1
    
    print('BST is Working...')
    