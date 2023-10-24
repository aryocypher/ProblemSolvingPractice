from ast import List
import math

# first solution


class Solution:
    def reverseString(self, s: List[str]) -> None:
        length = len(s)
        for i in range(math.floor(length/2)):
            s[i], s[length-i-1] = s[length-i-1], s[i]


# second solution
class Solution2:
    def reverseString(self, s: List[str]) -> None:
        s[:] = s[::-1]
