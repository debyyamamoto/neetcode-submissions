# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> int:
        resp = True
        def dfs(node):
            nonlocal resp
            if not node:
                return 0
            
            esquerda = dfs(node.left)
            direita = dfs(node.right)

            if abs(esquerda - direita) > 1:
                resp = False   

            return max(esquerda, direita) + 1

        dfs(root)
        return resp