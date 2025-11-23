class Solution(object):
    def maxSumDivThree(self, nums):
        s = 0
        m1 = [10**15, 10**15]
        m2 = [10**15, 10**15]

        for x in nums:
            s += x
            r = x % 3
            if r == 1:
                if x < m1[0]:
                    m1[1] = m1[0]
                    m1[0] = x
                elif x < m1[1]:
                    m1[1] = x
            elif r == 2:
                if x < m2[0]:
                    m2[1] = m2[0]
                    m2[0] = x
                elif x < m2[1]:
                    m2[1] = x

        rem = s % 3
        if rem == 0:
            return s

        if rem == 1:
            remove = min(
                m1[0],
                m2[0] + m2[1] if m2[1] < 10**15 else 10**15
            )
        else:
            remove = min(
                m2[0],
                m1[0] + m1[1] if m1[1] < 10**15 else 10**15
            )

        return 0 if remove >= 10**15 else s - remove