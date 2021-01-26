#速度は提出者の95%に負けてた
#メモリの使用量も提出者の90%に負け

#動的計画法を使うと良かったみたい

import numpy as np
import re

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :type output: List[int]
        """
        length = len(nums)
        array = []
        for i in range(length):
            array.append(nums)

        array = np.array(array)
        t_array = array.transpose()
        
        sum_result = array + t_array
        
        answer = ''
        for i in range(length - 1):
            for j in np.arange(i+1, length):
                if sum_result[i][j] == target:
                    answer = "[" + str(i) + "," + str(j) + "]"

        return answer

def main():
    solution = Solution()
    while True:
        nums_str = input()
        
        nums_list = re.split('[\[,\]]', nums_str)

        nums = []
        for num in nums_list:
            if num != '':
                try:
                    if int(num) >= -10**9 and int(num) <= 10**9:
                        nums.append(int(num))
                    else:
                        print("num is \"-10^9 <= num <= 10^9\"")
                        continue
                except ValueError as e:
                    print("input example: [1,2,4,7]")
                    continue
        
        length = len(nums)
        if length >= 2 and length <= 1000:
            break
        else:
            print("length of list is \"2 <= num <= 1000\"")

    while True:
        try:
            target = int(input())
        except ValueError as e:
            print("int only")
            continue

        if target >= -10**9 and target <= 10**9:
            break
        else:
            print("target is \"-10^9 <= target <= 10^9\"")
    
    answer = solution.twoSum(nums, target)
    print(answer)


if __name__ == "__main__":
    main()
