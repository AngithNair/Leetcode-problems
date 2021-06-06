#1480. Running Sum of 1d Array
from typing import List


class Solution:
    def runningsum(self, nums: List[int]) -> List[int]:
        ans = []
        ans.append(nums[0])
        for i in range(1,len(nums)):
            ans.append(ans[i-1] + nums[i])
        return ans