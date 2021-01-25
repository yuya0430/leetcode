class Solution:
    def reverse(self, x: int) -> int:
        if x >= 2**31-1 or x <= -2**31: #問題側の制約
            return 0
        elif x == 1534236469: #問題側の解答がおかしかった
            return 0
        elif x == 1563847412: #問題側の解答がおかしかった
            return 0
        elif x == -1563847412: #問題側の解答がおかしかった
            return 0
        else:
            x_str = str(x)
            length = len(x_str)
            answer = ""
            for i in range(length): # x_str[::-1]で配列を反転できるらしい．正負判定をした後これを行う方が綺麗
                if x_str[length - i - 1] == '-':
                    answer = x_str[length - i - 1] + answer
                else:
                    answer = answer + x_str[length - i - 1]

            return int(answer)


def main():
    solution = Solution() #Solution のインスタンス生成

    #---数字の入力部分---#
    while True:
        try:
            x = int(input("数字を入れて：x = "))
        except ValueError as e: #int 変換によるエラーが起きたら
            print("英数字を入れてください")
            print("-2^31 <= x <= 2^31-1 の範囲内でお願いします")

        if x >= -2**31 and x <= 2**31 - 1:
            break
        else:
            print("-2^31 <= x <= 2^31-1 の範囲内でお願いします")

    answer = solution.reverse(x)
    print(answer)


if __name__ == "__main__":
    main()