# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.maior_diametro = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0
            
            esquerda = dfs(node.left)
            direita = dfs(node.right)

            self.maior_diametro = max(self.maior_diametro, esquerda+direita)

            return max(esquerda, direita) + 1
        
        dfs(root)
        return self.maior_diametro   