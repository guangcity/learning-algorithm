class Solution(object):
    def flipgame(self, fronts, backs):
        """
        :type fronts: List[int]
        :type backs: List[int]
        :rtype: int
        """
        lens = len(fronts)
        ans = 9999
        dictnone = {}
        for i in range(lens):
            if(fronts[i] == backs[i]):
                dictnone[fronts[i]] = 1
        for i in range(lens):
            if not fronts[i] in dictnone.keys():
                ans = min(ans,fronts[i])
        for i in range(lens):
            if not backs[i] in dictnone.keys():
                ans = min(ans,backs[i])
        if ans == 9999 :
            return 0
        else :
            return ans