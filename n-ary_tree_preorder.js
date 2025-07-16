/**
 * // Definition for a _Node.
 * function _Node(val, children) {
 *    this.val = val;
 *    this.children = children;
 * };
 */

/**
 * @param {_Node|null} root
 * @return {number[]}
 */
var preorder = function(root) {
    
    var res = []
    const dfs = (root, res) => {
        if(!root){
            return;
        }
        res.push(root.val);

        root.children.forEach((child) =>{
            dfs(child, res);
        })
    }

    dfs(root, res);
    return res;
};