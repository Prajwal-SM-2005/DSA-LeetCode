class Solution(object):
    def countPalindromicSubsequence(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter=0
        for ch in set(s):
            l, r = s.find(ch), s.rfind(ch)
            if l < r:
                for mid in set(s[l+1:r]):
                    counter+=1
        return counter