#時間が足りない
#for 文が減っただけで，オーダは減ってない．見づらくなってるだけのダメなコード

#  (s)    (check_s)   (reverse_s)
# babad     dabab        dabab
# babad     abab         dabab
# babad     bab       dabab -> daba
# babad     daba         daba
# babad     aba       daba -> dab

# 結局O(n^2)という．．．

#一回目のチャレンジ（失敗）
""" 
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        else:
            output_length = 0
            reverse_s, check_s = s[::-1], s[::-1] #reverse_s: 後ろから削除していく，check_s: 前から削除していく

            while len(check_s) > output_length: #時間削減の工夫: 既に出ている答えより短いのを調べないように
                if check_s in s and check_s == check_s[::-1]:
                    # check_s in s だと "aabavwabaa" が入力の時 "aaba"を出力してしまう
                    # 対策として，check_s == check_s[::-1] を加えた
                    
                    #---出力文の更新---#
                    output = check_s 
                    output_length = len(check_s)

                    #---反対にした発話の最後の文字を消してもう一度探索を始める---#
                    reverse_s = reverse_s[:-1] 
                    check_s = reverse_s
                else:
                    check_s = check_s[1:]
                    if len(check_s) <= output_length: #時間削減の工夫

                        #---反対にした発話の最後の文字を消してもう一度探索を始める---#
                        reverse_s = reverse_s[:-1]
                        check_s = reverse_s

            return output
"""


#計算時間はちょうど半分くらい
#使用メモリも提出者の40%に勝っていた
class Solution:
    def palindrome_search(self, s: str, idx1: int, idx2: int, length: int) -> str:
        #---最初に設定した位置から左右に1つずつずらしていって左右対称か確認していく---#
        while idx1 >= 0 and idx2 <= length - 1 and s[idx1] == s[idx2]:
            idx1 -= 1
            idx2 += 1

        output = s[idx1+1:idx2]

        if output == output[::-1]: # "ba" が初期位置の場合は左右対称にならないのでその対策
            return output
        else:
            return ""

    def longestPalindrome(self, s: str) -> str:
        length = len(s)

        if length <= 1: #長さが1以下はそのまま返す
            return s
        
        output = ""
        for idx in range(length):
            output1 = self.palindrome_search(s, idx, idx, length) #長さが奇数の場合
            output2 = self.palindrome_search(s, idx, idx+1, length) #長さが偶数の場合に対応
            
            #---最大長のものをoutputに入れていく---#
            if len(output) < len(output1):
                output = output1
            if len(output) < len(output2):
                output = output2

        return output



def main():
    s = "babad"
    print(s[::-1])
    solution = Solution()

    output = solution.longestPalindrome(s)
    print(output)

if __name__ == "__main__":
    main()