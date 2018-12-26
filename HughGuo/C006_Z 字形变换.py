class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if len(s)<=numRows or numRows == 1:
            return s
        k = 2*numRows-2
        ans = ['']*numRows
        change = -1
        i = 0
        for char in s:
            if i == 0 or i == numRows -1:
                change = -change
            ans[i] += char
            i=i+change

        return ''.join(ans)
