class Solution:
    #Runtime: 28 ms, faster than 94.13% of Python3 online submissions for Longest Common Prefix.
    #Memory Usage: 14.5 MB, less than 29.18% of Python3 online submissions for Longest Common Prefix.
    def longestCommonPrefix(self, strs):
        """
        type strs: List[str]
        type return: str
        """
        if len(strs) == 0:
            return 0
        elif len(strs) == 1:
            return strs[0]

        strs = sorted(strs, reverse=False, key=lambda x: len(x))
        candidate = ''
        candidates = []
        i, j = -1, -1
        while i < len(strs[0])-1:
            i += 1
            j += 1
            if strs[0][i] == strs[1][j]:
                candidate += strs[0][i]
                if candidate not in candidates:
                    candidates = [candidate] + candidates
            else:
                break

        candidates = sorted(candidates, reverse=True, key=lambda x: len(x))
        print(candidates)
        
        for candidate in candidates:
            for i, s in enumerate(strs):
                if candidate == s[:len(candidate)]:
                    if i == len(strs)-1:
                        return candidate
                    continue
                else:
                    break

        return ''

    #難しく考えすぎた
    #こちらは先頭以外からも共通部分を探している
    def longestCommonPrefix2(self, strs):
        """
        type strs: List[str]
        type return: str
        """
        if len(strs) == 0:
            return 0
        elif len(strs) == 1:
            return strs[0]

        def str_indexes(s, c):
            output = []
            for i in range(len(s)):
                if s[i] == c:
                    output.append(i)
            return output

        strs = sorted(strs, reverse=False, key=lambda x: len(x))
        candidates = []
        for i, c in enumerate(strs[0]):
            indexes = str_indexes(strs[1], c)
            for j in indexes:
                candidate = c
                candidates.append(candidate)
                while i < len(strs[0])-1:
                    i += 1
                    j += 1
                    if strs[0][i] == strs[1][j]:
                        candidate += strs[0][i]
                        if candidate not in candidates:
                            candidates.append(candidate)
                    else:
                        break
        
        candidates = sorted(candidates, reverse=True, key=lambda x: len(x))
        
        for candidate in candidates:
            for i, s in enumerate(strs):
                if candidate in s:
                    if i == len(strs)-1:
                        return candidate
                    continue
                else:
                    break

        return ''

def main():
    strs = ["flower", "flow", "flight"]
    sol = Solution()
    output = sol.longestCommonPrefix(strs)
    print(output)

if __name__ == "__main__":
    main()