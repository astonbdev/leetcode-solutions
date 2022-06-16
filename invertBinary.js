/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {TreeNode}
 */
 var invertTree = function(root) {

  if(root === null){
      return root;
  }

  let temp = root.left;

  //base case left
  if(root.left !== null){
      root.left = invertTree(root.left);
  }

  //base case right
  if(root.right !== null){
      root.right = invertTree(root.right);

  }

  root.left = root.right;
  root.right = temp;

  return root;
};