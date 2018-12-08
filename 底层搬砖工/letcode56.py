# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

#该题主要是合并区间，先排序[l,r]队列，按照l升序，然后对l在其中的进行合并，不在其中的插入新的区间对继续操作。

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        ans = []
        lens = len(intervals)
        if lens<=0:
            return intervals
        intervals = sorted(intervals,key = lambda v: v.start)
        l = intervals[0].start
        r = intervals[0].end
        for p in range(lens):
            pl = intervals[p].start
            pr = intervals[p].end
            if pl <= r:
                r = max(r,pr)
            else:
                ans.append([l,r])
                l = pl
                r = pr
        ans.append([l,r])
        return ans