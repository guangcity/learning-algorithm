# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 方法一 中序遍历，然后判断
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        list = self.inorder(root)

        for i in range(len(list) - 1):
            if list[i] >= list[i + 1]:
                return False
        return True

    def inorder(self, root):
        if root is None:
            return []
        result_1 = [root.val]
        leftval_1 = self.inorder(root.left)
        rightval_1 = self.inorder(root.right)
        return leftval_1 + result_1 + rightval_1



# 方法二、递归

class Solution(object):
    def __init__(self):
        self.flag = True

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.judge(root, None, None)
        return self.flag

    def judge(self, root, min, max):
        if root is None:
            return
        if (min != None and root.val <= min.val) or (max != None and root.val >= max.val):
            self.flag = False
            return

        self.judge(root.left, min, root)  # 对于左子树而言，最大值是左子树的父节点root
        self.judge(root.right, root, max)  # 对于右子树而言，最小值是右子树的父节点root

# 方法三、中序遍历过程中进行判断

class Solution(object):

    def __init__(self):
        import sys
        self.last = -sys.maxint  # python中最小的数（本来是最大，加了个负号）

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        if root is None:
            return True

        if self.isValidBST(root.left) == False:  # 一边进行中序遍历，一边进行比较（中序遍历是递增数列），所以要设置全局变量，每遍历得到一个值便比较一次
            return False
        if root.val <= self.last:
            return False
        self.last = root.val
        if self.isValidBST(root.right) == False:
            return False
        return True

