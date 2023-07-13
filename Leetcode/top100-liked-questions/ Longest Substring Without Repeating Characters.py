class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l,r = 0,0
        length = 0
        check = ""
        while l <= r and r < len(s):
            if s[r] not in check:
                check += s[r]
                r += 1
                length = max(length, len(check))
            else:
                l += 1
                check = check[1:]
                
        return length

            