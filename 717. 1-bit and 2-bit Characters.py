class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        bits_len = len(bits)
        i = 0
        while i < bits_len-1:
            if bits[i] == 1:
                i += 2
            else:
                i += 1

        if i == bits_len-1 and bits[i] == 0:
            return True
        else:
            return False