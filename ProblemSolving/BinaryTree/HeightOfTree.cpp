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
    // Function to find the height of a binary tree using recursive Method.
    int heightByRecursiveMethod(struct TreeNode *node)
    {
        if (node == NULL)
        {
            return 0;
        }
        int leftHeight = heightByRecursiveMethod(node->left);
        int rightHeight = heightByRecursiveMethod(node->right);
        int maxHeight = max(leftHeight, rightHeight) + 1;
        return maxHeight;
    }
    // 2. In this method we use queue to calculate height. It is similar to level order traversal.
    //  Height variable with int value is used which gets incremented every time iteration completes a level.
    int heightByIterativeMethod(struct TreeNode *root)
    {
        int height = 0;
        queue<TreeNode *> q;
        if (root == NULL)
        {
            return 0;
        }
        q.push(root);
        while (!q.empty())
        {
            height += 1;
            int size = q.size();
            for (int i = 0; i < size; i++)
            {
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
        }
        return height;
    }
};