class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l,r = 0,len(height)-1
        result = 0
        while l < r:    # 두개의 끝점이 확실해야함블
            lh,rh = height[l],height[r]
            result =max( (r-l) * (min(lh,rh)), result)
            if lh >= rh:
                r -=1
            else:
                l += 1
        return result