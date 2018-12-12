

class Solution(object):
    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        这题可以思考为常数为单买，变数为礼包，只有礼包才能更新最小值，因此题目变成了求有限情况下礼包组合的最小值，暴力即可。
        """
        def check(a,b):
            for i in range(len(a)):
                if a[i]<b[i]:
                    return False
            return True
        sum = 0
        for i in range(len(needs)):
            sum+= needs[i]*price[i]
        for sp in special:
            if check(needs,sp):
                newneeds = []
                for k in range(len(needs)):
                    newneeds.append(needs[k]-sp[k])
                sum = min(sum,self.shoppingOffers(price,special,newneeds)+sp[-1])
        return sum