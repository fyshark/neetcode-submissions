/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        List<Integer> pre = new ArrayList<>();
        for (int num: preorder) {
            pre.add(num);
        }
        return build(pre, inorder);
    }

    private TreeNode build(List<Integer> preorder, int[] inorder) {
        if (inorder.length == 0) return null;
        int rootVal = preorder.remove(0);
        int idx = 0;
        TreeNode root = new TreeNode(rootVal);
        while (rootVal != inorder[idx]) {
            idx++;
        }
        root.left = build(preorder, Arrays.copyOfRange(inorder, 0, idx));
        root.right = build(preorder, Arrays.copyOfRange(inorder, idx+1, inorder.length));
        return root;
    }
}
