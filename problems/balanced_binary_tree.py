# https://leetcode.com/problems/balanced-binary-tree
class Solution(object):
    def isBalanced(self, root):
        return self.helper(root)

    def helper(self, node):
        if not node:
            return True

        left, right = self.helper(node.left), self.helper(node.right)

        if not left or not right or abs(left - right) > 1:
            return False

        return max(left, right) + 1
