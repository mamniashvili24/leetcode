# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def postorderTraversal(self, root):
        result = []
        if root.left is not None:
           result.extend(self.postorderTraversal(root.left))
        if root.right is not None:
           result.extend(self.postorderTraversal(root.right))

        return result