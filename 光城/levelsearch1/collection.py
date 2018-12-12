class Solution:
    def levelOrder(self, root):
        # write your code here
        res = []
        if not root:
            return res
        import collections
        queue = collections.deque()
        queue.append(root)
        # visited = set(root)
        while queue:
            length = len(queue)
            level_val = []
            for _ in range(length):
                node = queue.popleft()
                level_val.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level_val)
        return res