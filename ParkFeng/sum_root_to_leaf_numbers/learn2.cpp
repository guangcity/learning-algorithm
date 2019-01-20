/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    int ans=0;
    void dfs(TreeNode* p,int x){
        if(!p->left && !p->right){
            ans+=x*10+p->val;
            return;
        }
        if(p->left) dfs(p->left,x*10+p->val);
        if(p->right) dfs(p->right,x*10+p->val);
    }
    int sumNumbers(TreeNode* root) {
        if(!root) return 0;
        dfs(root,0);
        return ans;
    }
};