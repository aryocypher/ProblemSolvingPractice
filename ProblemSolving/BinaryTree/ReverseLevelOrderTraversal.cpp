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
    // Method 1: Using for loop with queue size known for each level
    // In the level order traversal we calculate size of queue before iterating over queue for each level.
    // In this case there is no need to put null value in queue as we know the size beforehand.
    vector<vector<int>> levelOrderWithQueueSizeCalculated(TreeNode *root)
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
            vector<int> levelRs(size);
            for (int i = 0; i < size; i++)
            {
                levelRs[i] = q.front()->val;
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
        reverse(rs.begin(), rs.end());
        return rs;
    }
};