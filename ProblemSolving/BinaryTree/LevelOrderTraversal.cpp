/**
 * Definition for a binary tree node.
 * */

#include <iostream>
#include <vector>
#include <queue>

using namespace std;

struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution
{
public:
    vector<vector<int>> levelOrder(TreeNode *root)
    {
        vector<vector<int>> rs;
        queue<TreeNode *> q;
        if (root == NULL)
        {
            return rs;
        }
        q.push(root);
        while (!q.empty())
        {
            int size = q.size();
            vector<int> levelRs;
            for (int i = 0; i < size; i++)
            {
                levelRs.push_back(q.front()->val);
                if (q.front()->left)
                {
                    q.push(q.front()->left);
                }
                if (q.front()->right)
                {
                    q.push(q.front()->right);
                }
                q.pop();
            }
            rs.push_back(levelRs);
        }
        return rs;
    }
};