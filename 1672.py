#1672. Richest Customer Wealth
from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        a = []
        for i in accounts:
            a.append(sum(i))
        return max(a)