#Runtime: 20 ms, faster than 99.39% of Python3 online submissions for Letter Combinations of a Phone Number.
#Memory Usage: 14.3 MB, less than 35.65% of Python3 online submissions for Letter Combinations of a Phone Number.
class Solution:
    def __init__(self):
        self.digit_map = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
    
    def letterCombinations(self, digits):
        """
        type digits: str \\
        type return: List[str] \\
        (ex.) "23" -> ["ad", "ae", "af", "bd", "be", ...]
        """
        
        if digits == "":
            return []

        def generate_combination(digits, before_list):
            if digits == "":
                return before_list
            else:
                digit = digits[0]
                output_list = []
                #---一気に複数個追加することで時短---#
                if digit in ["7", "9"]:
                    for s in before_list:
                        output_list += [s+self.digit_map[digit][0], s+self.digit_map[digit][1],
                            s+self.digit_map[digit][2], s+self.digit_map[digit][3]]
                    
                else:
                    for s in before_list:
                        output_list += [s+self.digit_map[digit][0], s+self.digit_map[digit][1],
                            s+self.digit_map[digit][2]]

                return generate_combination(digits[1:], output_list)
        

        return generate_combination(digits, [""])


def main():
    digits = "2387"
    sol = Solution()
    print(sol.letterCombinations(digits))

if __name__ == "__main__":
    main()