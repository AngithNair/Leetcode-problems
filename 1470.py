#1470. Shuffle the Array
from typing import List


class Solution:
    def Shuffle(self, nums: List[int], n: int) -> List[int]:
        a = []
        for i in range(0,n):
            a.append(nums[i])
            a.append(nums[i+n])
        return a