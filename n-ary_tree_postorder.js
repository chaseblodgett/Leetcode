/**
 * // Definition for a _Node.
 * function _Node(val,children) {
 *    this.val = val;
 *    this.children = children;
 * };
 */

/**
 * @param {_Node|null} root
 * @return {number[]}
 */
var postorder = function(root) {
    var res = []

    const postorder = (root, res) => {
        if(!root){
            return;
        }

        root.children.forEach((child) => {
            postorder(child, res);
        })

        res.push(root.val);
    }

    postorder(root, res);
    return res;

};