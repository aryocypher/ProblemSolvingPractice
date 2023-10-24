// Given two strings s and t, return true if t is an anagram of s, and false otherwise.

// An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

// Example 1:

// Input: s = "anagram", t = "nagaram"
// Output: true
// Example 2:

// Input: s = "rat", t = "car"
// Output: false

// Constraints:

// 1 <= s.length, t.length <= 5 * 104
// s and t consist of lowercase English letters.

// Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

// Note: We can use array of 24 size instead of unordered map here.
#include <iostream>
#include <unordered_map>

using namespace std;

class Solution
{
public:
    bool isAnagram(string s, string t)
    {
        unordered_map<char, int> sSet;
        for (int i = 0; i < s.size(); i++)
        {
            if (sSet.find(s[i]) == sSet.end())
            {
                sSet.insert({s[i], 1});
            }
            else
            {
                auto it = sSet.find(s[i]);
                it->second = it->second + 1;
            }
        }
        for (int i = 0; i < t.size(); i++)
        {
            if (sSet.find(t[i]) == sSet.end())
            {
                return false;
            }
            auto it = sSet.find(t[i]);
            if (it->second == 0)
            {
                return false;
            }
            it->second = it->second - 1;
        }
        for (auto it : sSet)
        {
            if (it.second > 0)
            {
                return false;
            }
        }
        return true;
    }
};