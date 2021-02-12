class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        #---first solution(時間切れ)---#
        """
        if len(height) <= 1:
            return 0
        elif len(height) == 2:
            return min(height[0], height[1])
        output = 0
        for i, y in enumerate(height):
            for j in range(i):
                output = max(output, min(y, height[j])*(i-j))

        return output
        """

        #---second solution---#
        #Runtime: 172 ms, faster than 62.33% of Python3 online submissions for Container With Most Water.
        #Memory Usage: 16.5 MB, less than 75.16% of Python3 online submissions for Container With Most Water.
        if len(height) <= 1:
            return 0
        elif len(height) == 2:
            return min(height[0], height[1])
        output, l, r = 0, 0, len(height)-1
        
        while l < r:
            output = max(output, min(height[l], height[r])*(r-l))

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return output
        

def main():
    height = [1,8,6,2,5,4,8,3,7]
    solution = Solution()
    output = solution.maxArea(height)
    print(output)

if __name__ == "__main__":
    main()