#速度は提出者の95%に負けてた
#メモリの使用量も提出者の90%に負け

#動的計画法を使うと良かったみたい

import numpy as np
import re

class Solution:
    def twoSum(self, nums, target):
        sum_dict = {}

        for idx, num in enumerate(nums):
            if num in sum_dict.keys():
                return [sum_dict[num], idx]
            sum_dict[target - num] = idx

        return []


    def twoSum2(self, nums, target):
        length = len(nums)
        array = []
        for i in range(length):
            array.append(nums)

        array = np.array(array)
        t_array = array.transpose()
        
        sum_result = array + t_array
        
        answer = []
        for i in range(length - 1):
            for j in np.arange(i+1, length):
                if sum_result[i][j] == target:
                    answer = [i,j]

        return answer

def main():
    nums = [2,7,11,15]
    target = 9
    solution = Solution()
    answer = solution.twoSum(nums, target)
    print(answer)


if __name__ == "__main__":
    main()
