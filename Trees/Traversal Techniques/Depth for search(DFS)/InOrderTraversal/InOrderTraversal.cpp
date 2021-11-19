#include <bits/stdc++.h>
using namespace std;

struct TreeNode{
    int data;
    struct TreeNode *right;
    struct TreeNode *left;

    TreeNode(int val){
        data=val;
        right=NULL;
        left=NULL;
    }
};
class Solution{
    private:
    void dfs(TreeNode*node,vector<int>&inorder){
        if(node==NULL)return ;
        dfs(node->left,inorder);
        inorder.push_back(node->data);
        dfs(node->right,inorder);
    }

    public:
    vector<int>inorderTraversal(TreeNode *root){
        vector<int>inorder;
        dfs(root,inorder);
        return inorder;
    }
};