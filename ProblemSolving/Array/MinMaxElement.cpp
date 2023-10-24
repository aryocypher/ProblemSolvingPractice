#include <iostream>

using namespace std;

class Solution
{
public:
    int findSum(int A[], int N)
    {
        int minElement = INT32_MAX;
        int maxElement = INT32_MIN;
        for (int i = 0; i < N; i++)
        {
            if (A[i] < minElement)
            {
                minElement = A[i];
            }
            if (A[i] > maxElement)
            {
                maxElement = A[i];
            }
        }
        return minElement + maxElement;
    }
};