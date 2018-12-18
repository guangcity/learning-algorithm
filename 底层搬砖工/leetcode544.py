class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        ans = []
        for p in range(len(wall)):
            x = wall[p]
            sum = 0
            for q in range(len(wall[p])):
                sum+= wall[p][q]
                if q != len(wall[p])-1:
                    ans.append(sum)
        ans.sort()
        ans2 = 0
        nowmax = 0
        before = -1
        for i in range(len(ans)):
            if before == ans[i]:
                nowmax+=1
            else:
                nowmax=1
                before = ans[i]
            ans2= max(ans2,nowmax)
        return len(wall)-ans2