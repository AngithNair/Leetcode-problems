#1880. Check if Word Equals Summation of Two Words
class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        letters_value = {letter: value for value, letter in enumerate('abcdefghij')}
        return int(''.join(str(letters_value[letter]) for letter in firstWord)) + int(''.join(str(letters_value[letter]) for letter in secondWord)) == int(''.join(str(letters_value[letter]) for letter in targetWord))