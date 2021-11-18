#include <bits/stdc++.h>
using namespace std;
struct TreeNode{
    int data;
    struct TreeNode* left;
    struct TreeNode* right;

    TreeNode(int val){
        data=val;

        left=NULL;
        right=NULL;

    }
};

class Solution {
    private:
    void dfs(TreeNode *node, vector<int> &preorder) {
        if(node == NULL) return; 
        
        preorder.push_back(node->data); 
        dfs(node->left, preorder); 
        dfs(node->right, preorder); 
    }
public:
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> preorder;
        dfs(root, preorder);
        return preorder; 
    }
};
