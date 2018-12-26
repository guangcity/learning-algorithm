class Solution:
    def levelOrder(self, root):
        # write your code here
        res = []
        if not root:
            return []
        res_list = []
        root_list = [root]
        while root_list and len(root_list)!=0:
            val_list = []
            level_list = []
            for node in root_list:
                val_list.append(node.val)
                if node.left:
                    level_list.append(node.left)
                if node.right:
                    level_list.append(node.right)
            root_list = level_list
            res_list.append(val_list)
        return res_list