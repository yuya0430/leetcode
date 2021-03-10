#Runtime: 44 ms, faster than 83.95% of Python3 online submissions for Roman to Integer.
#Memory Usage: 14.4 MB, less than 29.65% of Python3 online submissions for Roman to Integer.
class Solution:
    def romanToInt(self, s: str) -> int:
        def check(c1, c2):
            """
            type c1: char \\
            type c2: char \\
            type return: boolean
            """
            if c1 == 'C':
                return c2 == 'M' or c2 == 'D' #CM CDになってるかを返す
            elif c1 == 'X':
                return c2 == 'C' or c2 == 'L' #XC XLになってるかを返す
            elif c1 == 'I':
                return c2 == 'X' or c2 == 'V' #IX IVになってるかを返す

        output = 0
        i = 0
        map_roman = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        while i < len(s)-1:
            if check(s[i], s[i+1]):
                output += map_roman[s[i+1]] - map_roman[s[i]]
                i += 2
            else:
                output += map_roman[s[i]]
                i += 1

        if i == len(s):
            return output
        else:
            return output + map_roman[s[i]]


        

def main():
    num = 'MCMXCIV'
    sol = Solution()
    output = sol.romanToInt(num)
    print(output)

if __name__ == "__main__":
    main()