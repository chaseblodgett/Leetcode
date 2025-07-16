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
 * @return {number[]}
 */
var averageOfLevels = function(root) {
    
    let q = [];
    if(root){
        q.push(root);
    }
    let ret = []
    while(q.length > 0){
        let size = q.length;
        let sum = 0;
        for(let i = 0; i < size; i++){
            let node = q.shift();
            sum += node.val;
            if(node.left){
                q.push(node.left);
            }
            if(node.right){
                q.push(node.right);
            }
        }
        ret.push(sum / size);
    }

    return ret;
};