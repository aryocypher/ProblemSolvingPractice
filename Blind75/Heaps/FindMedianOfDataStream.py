# 295. Find Median from Data Stream
# Solved
# Hard
# Topics
# Companies
# The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

# For example, for arr = [2,3,4], the median is 3.
# For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
# Implement the MedianFinder class:

# MedianFinder() initializes the MedianFinder object.
# void addNum(int num) adds the integer num from the data stream to the data structure.
# double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.


# Example 1:

# Input
# ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
# [[], [1], [2], [], [3], []]
# Output
# [null, null, null, 1.5, null, 2.0]

# Explanation
# MedianFinder medianFinder = new MedianFinder();
# medianFinder.addNum(1);    // arr = [1]
# medianFinder.addNum(2);    // arr = [1, 2]
# medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
# medianFinder.addNum(3);    // arr[1, 2, 3]
# medianFinder.findMedian(); // return 2.0


# Constraints:

# -105 <= num <= 105
# There will be at least one element in the data structure before calling findMedian.
# At most 5 * 104 calls will be made to addNum and findMedian.


# Follow up:

# If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
# If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?

class MedianFinder:

    def __init__(self):
        self.smallHeap = []
        self.largeHeap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.smallHeap, -1*num)
        if self.smallHeap and self.largeHeap and (self.smallHeap[0]*-1) > self.largeHeap[0]:
            val = -1 * heapq.heappop(self.smallHeap)
            heapq.heappush(self.largeHeap, val)

        if len(self.smallHeap) > len(self.largeHeap)+1:
            val = -1 * heapq.heappop(self.smallHeap)
            heapq.heappush(self.largeHeap, val)

        if len(self.largeHeap) > len(self.smallHeap)+1:
            val = heapq.heappop(self.largeHeap)
            heapq.heappush(self.smallHeap, -1*val)

    def findMedian(self) -> float:
        if len(self.smallHeap) > len(self.largeHeap):
            return -1 * self.smallHeap[0]

        if len(self.largeHeap) > len(self.smallHeap):
            return self.largeHeap[0]

        return (self.largeHeap[0]+(-1*self.smallHeap[0]))/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
