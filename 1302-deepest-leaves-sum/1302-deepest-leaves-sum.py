# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        queue = deque([[root, 0]])
        ans = [0, 0]
        while queue:
            node, level = queue.popleft()
            if level > ans[1]:
                ans[0], ans[1] = node.val, level
            elif level == ans[1]:
                ans[0] += node.val
            if node.left:
                queue.append([node.left, level+1])
            if node.right:
                queue.append([node.right, level+1])
        return ans[0]