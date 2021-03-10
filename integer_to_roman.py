class Solution:
    #Runtime: 48 ms, faster than 75.18% of Python3 online submissions for Integer to Roman.
    #Memory Usage: 14.3 MB, less than 31.37% of Python3 online submissions for Integer to Roman.
    def intToRoman(self, num: int) -> str:

        def gen_roman_parts(num, roma1, roma2, roma3):
            """
            type num: integer, [0:9]\\
            type roma1: str (ex. [I, X, C]) \\
            type roma2: str (ex. [V, L, D]) \\
            type roma3: str (ex. [X, C, M])
            """
            if num == 9:
                return roma1 + roma3
            elif num == 4:
                return roma1 + roma2
            elif num >= 5:
                return roma2 + roma1*(num-5)
            elif num >= 1:
                return roma1 * num
        
        output = ""
        while num >= 1000:
            num -= 1000
            output += "M"
        if num >= 100:
            output += gen_roman_parts(num//100, 'C', 'D', 'M')
            num -= (num//100) * 100
        if num >= 10:
            output += gen_roman_parts(num//10, 'X', 'L', 'C')
            num -= (num//10) * 10
        if num > 0:
            output += gen_roman_parts(num, 'I', 'V', 'X')

        return output

    def intToRoman2(self, num: int) -> str: #他人の解答（結果はどっこいどっこい）
        
        def getStr(dig, pos):
            if dig < 4:
                return num_map[1][pos] * dig
            elif dig == 4:
                return num_map[1][pos] + num_map[5][pos]
            elif dig < 9:
                return num_map[5][pos] + num_map[1][pos] * (dig - 5)
            elif dig == 9:
                return num_map[1][pos] + num_map[1][pos + 1]
            else:
                return ""
        
        
        num_map = {
            1: ['I', 'X', 'C', 'M'],
            5: ['V', 'L', 'D']
        }
        
        ans = []
        pos = 0
        while num:
            ans.append(getStr(num % 10, pos))
            num = num // 10
            pos += 1
        return ''.join(ans[::-1])

def main():
    num = 3863
    sol = Solution()
    output = sol.intToRoman(num)
    print(output)

if __name__ == "__main__":
    main()