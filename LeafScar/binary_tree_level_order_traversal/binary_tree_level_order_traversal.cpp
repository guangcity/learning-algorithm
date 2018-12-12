/*
 * Ⅰ.可以看成广度优先遍历
 * 创建一个队列
 *
 *     3
 *    / \
 *   9  20
 *     /  \
 *    15   7
 * 从根节点开始设为当前节点
 * 以下是队列的先入先出演示：
 *
 * 队列初始化，将根节点先入队
 * (1) 3
 * 访问时将当前节点出队，并将当前节点的左子与右子顺次入队
 *                                出队顺序
 * (2) |20 9|      3(出)              3
 * (3) |20|        9(出)              9
 * (4) |7 15|      20(出)             20
 * (5) |7|         15(出)             15
 * (6) ||          7(出)              7
 *
 * 该算法可以以迭代的形式实现
 * 1.将当前节点赋值为队顶节点并访问
 * 2.将当前节点的左子入队
 * 3.将当前节点的右子入队
 *
 * ☆.每次都是一层节点顺次入队完，再顺次入队该层节点的子节点，顺序不会打乱
 * 队列的特点是先入先出
 *
 *
 * Ⅱ.上述方法只能按层顺次访问，却无法分层，不能达到题目结果
 * 故，需要标记每一层的最后一个节点，当访问到时，即完成一层的访问，push到返回结果
 *
 * Ⅰ中☆所述: 可以当访问完该层最后一个节点时，
 *            同时会将最后一个节点的左子右子入队，
 *            最后一个节点的右子正好是下一层的最后一个节点，
 *            即可获得标记节点
 *
 * 通过该标记节点起到分层作用，每次迭代更新
 */
#include <vector>
#include <queue>
using namespace std;

struct TreeNode {
	int val;
	TreeNode* left;
	TreeNode* right;
	TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class Solution {
public:
	vector<vector<int>> levelOrder(TreeNode* root) {
		vector<vector<int>> rel;

		if (root == nullptr)
			return rel;

		queue<TreeNode*> tempQueue;

		tempQueue.push(root);
		TreeNode* lastNode = root;		// 记录当前层的最后一个元素，即上一层顺次最后一个节点，push到队列中的最后一个孩子
		TreeNode* lastNodeSign = root;	// 存储下一层的最后一个节点
		vector<int> levelInt;
		while (!tempQueue.empty())
		{
			TreeNode* x = tempQueue.front();
			tempQueue.pop();

			levelInt.push_back(x->val);	// 存储访问元素的值

			if (x->left != nullptr)
			{
				tempQueue.push(x->left);	// 存入当前节点左子
				lastNodeSign = x->left;		// 存入当前节点左子后，其正好为下一层的最后一个节点
			}

			if (x->right != nullptr)
			{
				tempQueue.push(x->right);	// 存入当前节点右子
				lastNodeSign = x->right;	// 下一层的最后一个节点变为其右子
			}

			if (x == lastNode)				// 当访问到当前层最后一个元素时，
			{
				lastNode = lastNodeSign;	// 更新lastNode为下一层的最后一个元素
				rel.push_back(levelInt);	// levelInt已经包含当前层的所有值，存入返回结果中
				levelInt.clear();			// 清空levelInt，准备记录下一层的值
			}
		}

		return rel;
	}
};
