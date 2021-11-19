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
    void dfs(TreeNode *node,vector<int>&postnode){
        if(node=NULL)return ;
        dfs(node->right,postnode);
        dfs(node->left,postnode);
        postnode.push_back(node->data);
    }

    public:
    vector<int>postorderTraversal(TreeNode *root){
        vector<int>postorder;
        dfs(root,postorder);
        return postorder;
    }
};