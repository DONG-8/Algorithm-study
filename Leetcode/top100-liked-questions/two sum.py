
## 나의 풀이 two pointer
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 1만 n^2 10^8 시간복잡도 높음
        # 투포인터를 이용한 풀이
        # 배열 정렬하기
        index_info_nums = []
        for i in range(len(nums)):
            index_info_nums.append((nums[i],i))
        index_info_nums.sort()
        l,r = 0,len(nums)-1
        while l < r:
            tar = index_info_nums[l][0] + index_info_nums[r][0]
            if tar >= target:
                if tar == target:
                    break
                r -= 1
            else:
                l += 1 
        return [index_info_nums[l][1],index_info_nums[r][1]]

# 릿코드 풀이 해시맵

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i