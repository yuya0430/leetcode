#Runtime: 88 ms, faster than 17.58% of Python3 online submissions for Palindrome Number.
#Memory Usage: 14.4 MB, less than 18.73% of Python3 online submissions for Palindrome Number.


#---元々作成していた longest_palindromic_substring.py を利用した---#
class Solution:
    def palindrome_search(self, s: str, idx1: int, idx2: int, length: int) -> str:
        #---最初に設定した位置から左右に1つずつずらしていって左右対称か確認していく---#
        while idx1 >= 0 and idx2 <= length - 1 and s[idx1] == s[idx2]:
            idx1 -= 1
            idx2 += 1

        output = s[idx1+1:idx2]

        if output == s: # "ba" が初期位置の場合は左右対称にならないのでその対策
            return True
        else:
            return False

    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        length = len(s)
        half_length = length / 2

        if half_length % 1 == 0:
            i = int(half_length)
            return self.palindrome_search(s, i-1, i, length)
        else:
            i = int(half_length)
            return self.palindrome_search(s, i, i, length)



def main():
    x = 121
    solution = Solution()
    output = solution.isPalindrome(x)
    print(output)

if __name__ in "__main__":
    main()