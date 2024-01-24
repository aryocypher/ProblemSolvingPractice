# Description
# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.)

# Only $39.9 for the "Twitter Comment System Project Practice" within a limited time of 7 days!

# WeChat Notes Twitter for more information（WeChat ID jiuzhangfeifei）


# (0,8),(8,10) is not conflict at 8

# Example
# Example1

# Input: intervals = [(0,30),(5,10),(15,20)]
# Output: 2
# Explanation:
# We need two meeting rooms
# room1: (0,30)
# room2: (5,10),(15,20)
# Example2

# Input: intervals = [(2,7)]
# Output: 1
# Explanation:
# Only need one meeting room


from typing import (
    List,
)
from lintcode import (
    Interval,
)
import heapq
"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """

    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x.start)

        rooms = [intervals[0].end]
        heapq.heapify(rooms)

        for interval in intervals[1:]:
            if interval.start >= rooms[0]:
                heapq.heappop(rooms)
            heapq.heappush(rooms, interval.end)

        return len(rooms)
