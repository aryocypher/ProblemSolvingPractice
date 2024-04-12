# 2013. Detect Squares
# Medium
# Topics
# Companies
# Hint
# You are given a stream of points on the X-Y plane. Design an algorithm that:

# Adds new points from the stream into a data structure. Duplicate points are allowed and should be treated as different points.
# Given a query point, counts the number of ways to choose three points from the data structure such that the three points and the query point form an axis-aligned square with positive area.
# An axis-aligned square is a square whose edges are all the same length and are either parallel or perpendicular to the x-axis and y-axis.

# Implement the DetectSquares class:

# DetectSquares() Initializes the object with an empty data structure.
# void add(int[] point) Adds a new point point = [x, y] to the data structure.
# int count(int[] point) Counts the number of ways to form axis-aligned squares with point point = [x, y] as described above.
 
# class DetectSquares:

#     def __init__(self):
#       self.pts= defaultdict(int)

#     def add(self, point: List[int]) -> None:
#       self.pts[tuple(point)] += 1

#     def count(self, point: List[int]) -> int:
#       ans = 0
#       px, py = point

#       for x,y in self.pts:
#         dx = abs(px - x)
#         dy = abs(py - y)

#         if dx > 0 and dy > 0 and dx == dy:
#           if (x, py) in self.pts and (px, y) in self.pts:
#             ans += self.pts[(x, py)] * self.pts[(px, y)] * self.pts[(x, y)]

#       return ans
        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)