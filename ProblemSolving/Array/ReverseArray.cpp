#include <iostream>
#include <vector>

using namespace std;

class Solution
{
public:
    void reverseString(vector<char> &s)
    {
        int len = s.size();
        for (int i = 0; i < s.size() / 2; i++)
        {
            swap(s[i], s[len - 1 - i]);
        }
    }
};