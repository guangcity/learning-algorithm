class Solution {
    public boolean leafSimilar(TreeNode root1, TreeNode root2) {
        List<Integer> l1 = new LinkedList<>();
        List<Integer> l2 = new LinkedList<>();

        search(root1,l1);
        search(root2,l2);

        if(l1.size()!=l2.size()){
            return false;
        }

        for(int i = 0;i < l1.size();i++) {
        	if(l1.get(i)!=l2.get(i)){
                return false;
            }
        }
        return true;
    }

	public void search(TreeNode root,List<Integer> res) {
		if(root == null){
            return;
        }
		search(root.left,res);
		search(root.right,res);

		if(root.left == null && root.right == null){
            res.add(root.val);
        }
	}
}