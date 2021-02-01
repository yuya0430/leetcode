#計算速度は64ms 51.94%に勝利
#メモリ使用量は14.5MB 47.45%に勝利

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        output_list = [""] * numRows
        
        output = ""
        flag = 1
        idx = -1
        for char in s:
            if flag: #ジグザグの下に移動するとき
                idx += 1
                output_list[idx] += char
                if idx == numRows - 1: #最下層にきたらフラグを切り替える
                    flag = 0
            else: #ジグザグの上に移動するとき
                idx -= 1
                output_list[idx] += char
                if idx == 0:
                    flag = 1 #最上層にきたらフラグを切り替える

        
        for output_parts in output_list:
            output += output_parts

        return output
        

def main():
    s = "PAYPALISHIRING"
    numRows = 4

    solution = Solution()
    output = solution.convert(s, numRows)
    print(output)


if __name__ in "__main__":
    main()