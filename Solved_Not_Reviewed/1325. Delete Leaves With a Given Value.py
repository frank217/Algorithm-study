#https://leetcode.com/problems/delete-leaves-with-a-given-value/description/


class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:

        def recurse(node,target):
            if node.left and recurse(node.left,target):
                node.left = None
            if node.right and recurse(node.right,target):
                node.right = None

            if not node.left and not node.right and node.val == target:
                return True
            return False
        if root and recurse(root,target):
            return None
        return root

            