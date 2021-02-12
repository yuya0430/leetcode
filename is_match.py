import re

#Runtime: 60 ms, faster than 47.62% of Python3 online submissions for Regular Expression Matching.
#Memory Usage: 14.3 MB, less than 60.22% of Python3 online submissions for Regular Expression Matching.
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        result = re.match(p, s)
        if result == None:
            return False
        
        if result.group() == s:
            return True

    def isMatch2(self, text, pattern): #解答（動的計画法）なかなか理解できない
        memo = {}
        def dp(i, j):
            print(memo)
            print(i)
            print(j)
            input("1:")
            if (i, j) not in memo:
                if j == len(pattern):
                    ans = i == len(text)
                    print(ans)
                    print("2:")
                else:
                    first_match = i < len(text) and pattern[j] in {text[i], '.'} #文字が一致もしくは '.' であるか
                    print(first_match)
                    #---パターンの次の文字が'*'ならば---#
                    if j+1 < len(pattern) and pattern[j+1] == '*':
                        #---2個先のパターンを調べる．そしてテキストがpaturn[j]の文字で続いているか確認
                        ans = dp(i, j+2) or first_match and dp(i+1, j)
                        print(i)
                        print(j)
                        print(ans)
                        input("3:")
                    else:
                        #---次のテキストの文字，パターンの文字が一致しているか調べる---#
                        ans = first_match and dp(i+1, j+1)
                        print(i)
                        print(j)
                        print(ans)
                        input("4:")

                memo[i, j] = ans
                print(memo)
            return memo[i, j]

        return dp(0, 0)
        

def main():
    s = "aab"
    p = "c*a*b"
    #s = "aa"
    #p = "a*"
    solution = Solution()

    output = solution.isMatch2(s, p)
    print(output)

if __name__ == "__main__":
    main()
