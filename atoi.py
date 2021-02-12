#計算速度は提出者の10%に勝利
#使用メモリは提出者の60%に勝利

import re

class Solution:
    #--- 正規表現でやる作戦はいろんなパターンを想定する必要があって面倒かも---#
    """def myAtoi(self, s: str) -> int:
        if re.match(r'\s*([a-z\.]+|[+-]{2})', s):
            return 0

        result = re.search(r'[+-]?\d+', s)
        if result:
            output = int(result.group())
            if output > -2 ** 31 and output < 2 ** 31 - 1:
                return output
            else:
                if output > 0:
                    return 2 ** 31 - 1
                else:
                    return -2 ** 31
        else:
            return 0"""

    def myAtoi(self, s: str) -> int:
        if not re.search(r'\d+', s):
            return 0
        
        str_output = ""
        flag = True
        for char in s:
            if flag: # "+-"や数字が見つかるまでの処理，見つかれば下の処理に移動
                if char == " ":
                    continue
                elif char == "+" or char == "-":
                    str_output += char
                    flag = False
                elif re.match(r'\d', char):
                    str_output += char
                    flag = False
                else:
                    break
            else: #数字以外が見つかったらbreakされる仕組み
                if re.match(r'\d', char):
                    str_output += char
                else:
                    if not re.search(r'\d+', s): #数字が一つも入っていない場合は0とする
                        return 0
                    break
        
        if str_output:
            output = int(str_output)
            if output > -2 ** 31 and output < 2 ** 31 - 1:
                return output
            else:
                if output > 0:
                    return 2 ** 31 - 1
                else:
                    return -2 ** 31
        else:
            return 0
        

def main():
    s = "+-42"
    solution = Solution()
    output = solution.myAtoi(s)
    print(output)

if __name__ == "__main__":
    main()