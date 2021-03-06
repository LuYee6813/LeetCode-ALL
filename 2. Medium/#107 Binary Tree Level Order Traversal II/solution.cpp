void dfs(TreeNode* root, int depth, vector<vector<int>>& result) {
    if(root == nullptr){
        return;
    }
    if(depth == result.size()) {
        result.push_back({});
    }
    
    result[depth].push_back(root->val);
    
    dfs(root->left,depth+1,result);
    dfs(root->right, depth+1,result);
}
class Solution {
public:
    vector<vector<int>> levelOrderBottom(TreeNode* root) {
        vector<vector<int>> result;
        dfs(root, 0, result);
        reverse(begin(result), end(result));
        return result;
    }
};