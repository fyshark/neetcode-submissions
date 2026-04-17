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
        Deque<Integer> preorderDeque = new ArrayDeque<>();
        for (int val: preorder) {
            preorderDeque.offer(val);
        }
        return build(preorderDeque, inorder);
    }

    private TreeNode build(Deque<Integer> preorder, int[] inorder) {
        if (inorder.length > 0) {
            int idx = indexOf(inorder, preorder.poll());
            TreeNode root = new TreeNode(inorder[idx]);
            root.left = build(preorder, Arrays.copyOfRange(inorder, 0, idx));
            root.right = build(preorder, Arrays.copyOfRange(inorder, idx + 1, inorder.length));

            return root;
        }
        return null;
    }

    private int indexOf(int[] inorder, int value) {
        for (int i = 0; i < inorder.length; i++) {
            if (inorder[i] == value) {
                return i;
            }
        }
        return -1;
    }
}
