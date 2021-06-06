#1119. Remove Vowels from a String
class Solution:
    def removevowels(self, s: str) -> str:
        result = ""
        for char in s:
            if char not in ('a','e','i','o','u'):
                result += char
        return result