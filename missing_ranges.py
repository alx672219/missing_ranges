from typing import List

class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        nums = [lower-1] + nums + [upper+1]   # the reason lower - 1 is that when nums = [], lower = 1, upper = 1, res should be [1]
        res = []
        
        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] == 2:   # when interval is 1
                res.append(str(nums[i]+1))
            elif nums[i+1] - nums[i] > 2:
                res.append(str(nums[i]+1)+'->'+str(nums[i+1]-1))   # when interval is greater than 1
        
        return res