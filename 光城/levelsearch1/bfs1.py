class Solution:
    def levelOrder(self, root):
        # write your code here
        res = []

        if root is None:
            return res
        queue = [root]
        # 列表为空时，循环终止
        while queue and len(queue) != 0:
            # 使用列表存储同层节点
            level_val = []
            # 同层节点的个数
            length = len(queue)
            for i in range(length):
                # 将同层节点依次出队
                h = queue.pop(0)
                if h.left:
                    # 左孩子入队
                    queue.append(h.left)
                if h.right:
                    # 右孩子入队
                    queue.append(h.right)
                level_val.append(h.val)
            res.append(level_val)
        return res


