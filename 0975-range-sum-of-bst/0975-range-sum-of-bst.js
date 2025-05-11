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
 * @param {number} low
 * @param {number} high
 * @return {number}
 */
var rangeSumBST = function(root, low, high) {
    let values = [];
    let node = root;
    let stack =[];
    let s = 0;
    while (node || stack.length>0 ) {
        while (node) {
            stack.push(node);
            node = node.left;
        }

        node = stack.pop();
        values.push(node.val);
        node = node.right;
    }

    for (let j=0; j<=values.length; j++) {
        if (values[j]>=low && values[j]<=high) {
            s+=values[j];
        }
    }
    return s;
};