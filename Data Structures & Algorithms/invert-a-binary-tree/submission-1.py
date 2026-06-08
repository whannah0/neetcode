# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # pre-order traversal

        # no root
        if not root:
            return root
        #if root doesn't have any children
        if not root.left and not root.right:
            return root

        l = root.left
        r = root.right
        # root.left = r
        # root.right = l

        root.left = self.invertTree(r)
        root.right = self.invertTree(l)

        return root
        