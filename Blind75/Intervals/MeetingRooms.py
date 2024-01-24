# 920 · Meeting Rooms
# Algorithms
# Easy
# Accepted Rate
# 50%

# Description
# Solution93
# Notes
# Discuss99+
# Leaderboard
# Record
# Description
# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

# Only $39.9 for the "Twitter Comment System Project Practice" within a limited time of 7 days!

# WeChat Notes Twitter for more information（WeChat ID jiuzhangfeifei）


# (0,8),(8,10) is not conflict at 8

# Example
# Example1

# Input: intervals = [(0,30),(5,10),(15,20)]
# Output: false
# Explanation:
# (0,30), (5,10) and (0,30),(15,20) will conflict
# Example2

# Input: intervals = [(5,8),(9,15)]
# Output: true
# Explanation:
# Two times will not conflict

from typing import (
    List,
)
from lintcode import (
    Interval,
)

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
    @return: if a person could attend all meetings
    """

    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
        # Write your code here
        sortedIntervals = sorted(intervals, key=lambda x: x.end)

        for i in range(1, len(sortedIntervals)):
            if sortedIntervals[i].start < sortedIntervals[i-1].end:
                return False

        return True
