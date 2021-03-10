class Solution:
    #Runtime: 28 ms, faster than 85.30% of Python3 online submissions for Valid Parentheses.
    #Memory Usage: 14.3 MB, less than 66.49% of Python3 online submissions for Valid Parentheses.
    def __init__(self):
        self.parentheses_map = {
            "(": ")",
            "{": "}",
            "[": "]",
        }

    def isValid(self, s: str) -> bool: 
        """
        :type s: str
        :rtype: bool
        """
        if s[0] not in self.parentheses_map.keys():
            return False

        count = [0, 0, 0]
        search_pairs = []
        for c in s:
            if c in [")", "}", "]"] and len(search_pairs) == 0:
                return False

            if c == "(":
                count[0] += 1
                search_pairs += [self.parentheses_map[c]]
            elif c == ")":
                if search_pairs[-1] != c:
                    return False
                count[0] -= 1
                search_pairs.pop()
            elif c == "{":
                count[1] += 1
                search_pairs += [self.parentheses_map[c]]
            elif c == "}":
                if search_pairs[-1] != c:
                    return False
                count[1] -= 1
                search_pairs.pop()
            elif c == "[":
                count[2] += 1
                search_pairs += [self.parentheses_map[c]]
            elif c == "]":
                if search_pairs[-1] != c:
                    return False
                count[2] -= 1
                search_pairs.pop()
        
        if count == [0,0,0]:
            return True
        else:
            return False


def main():
    s = "(){}}{"
    sol = Solution()
    print(sol.isValid(s))

if __name__ == "__main__":
    main()