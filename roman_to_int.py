class Solution:
    def romanToInt(self, s: str) -> int:
        numerals = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        sum = 0
        i = 0

        while i < len(s):
            if(i + 1 >= len(s)):
                sum += numerals[s[i]]

            elif numerals[s[i]] < numerals[s[i+1]]:
                sum += numerals[s[i+1]] - numerals[s[i]]
                i += 1

            else:
                sum += numerals[s[i]]
            i += 1

        return sum