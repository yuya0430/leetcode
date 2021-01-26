class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1: #入力文字列の長さが1以下の時の処理
            return len(s)
        else: #入力文字列の長さが2以上の時の処理
            output_substring = ""
            substring = ""
            for char in s:
                if char not in substring: # substring に同じ文字がないときは追加
                    substring += char

                else:
                    if len(output_substring) < len(substring): #一番長い substring に更新
                        output_substring = substring
                    
                    index = substring.index(char) # 同じ文字があるインデックスを取得
                    substring = substring[index+1:] + char
                    #同じ文字がある箇所より後ろの文字列に文字を足して新たな substring の作成を始める
                    #例) dv + d -> vd

            return max(len(output_substring), len(substring))

        


def main():
    s = "dvdf"
    solution = Solution()

    output = solution.lengthOfLongestSubstring(s)
    print(output)

if __name__ == "__main__":
    main()