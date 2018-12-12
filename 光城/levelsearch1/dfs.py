class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        self.result = []
        self.dfs(root, 0)
        return self.result
    def dfs(self, root, level):
        if len(self.result) < level + 1:
            self.result.append([])
        self.result[level].append(root.val)
        if root.left:
            self.dfs(root.left, level + 1)
        if root.right:
            self.dfs(root.right, level + 1)