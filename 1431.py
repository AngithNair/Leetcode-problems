#1431. Kids With the Greatest Number of Candies
from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        a = []
        for i in range (0,len(candies)):
            x = extraCandies + candies[i]
            if x >= max_candies:
                a.append(True)
            else:
                a.append(False)
        return a