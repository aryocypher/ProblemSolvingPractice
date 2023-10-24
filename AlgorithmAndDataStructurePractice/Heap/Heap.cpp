#include <iostream>
#include <vector>
using namespace std;

class MinHeap
{
public:
    vector<int> v;
    void insertElement(int el)
    {
        if (v.empty())
        {
            v.push_back(-1);
        }
        v.push_back(el);
        int elIndex = v.size() - 1;
        int parent = elIndex / 2;
        while (elIndex > 1 && v[elIndex] < v[parent])
        {
            swap(v[elIndex], v[parent]);
            elIndex = parent;
            parent = parent / 2;
        }
    }

    void heapify(int i)
    {
        int left = 2 * i;
        int right = 2 * i + 1;
        int minIndex = i;
        if (left < v.size() and v[left] < v[i])
        {
            minIndex = left;
        }
        if (right < v.size() and v[right] < v[minIndex])
        {
            minIndex = right;
        }
        if (i != minIndex)
        {
            swap(v[i], v[minIndex]);
            heapify(minIndex);
        }
    }
    int getMin()
    {
        int el = v[1];
        return getMin();
    }

    void popMin()
    {
        int el = v[1];
        swap(v[1], v[v.size() - 1]);
        v.pop_back();
        heapify(1);
    }
};
