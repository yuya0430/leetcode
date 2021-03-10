class Solution2:
    def fourSum(self, nums, target):
        def kSum(nums, target, k):
            if len(nums) == 0 or nums[0] * k > target or target > nums[-1] * k:
                return []
            if k == 2:
                print(nums)
                print(target)
                print(k)
                input("c")
                return twoSum(nums, target)
            res = []
            for i in range(len(nums)):
                if i == 0 or nums[i - 1] != nums[i]:
                    print(nums)
                    print(target)
                    print(k)
                    input("a")
                    output = kSum(nums[i + 1:], target - nums[i], k - 1)
                    print(output)
                    input("b")
                    for _, set in enumerate(output):
                        res.append([nums[i]] + set)
            return res

        def twoSum(nums, target):
            res = []
            s = set()
            for i in range(len(nums)):
                if len(res) == 0 or res[-1][1] != nums[i]:
                    if target - nums[i] in s:
                        res.append([target - nums[i], nums[i]])
                s.add(nums[i])
            return res

        nums.sort()
        return kSum(nums, target, 4)

class Solution:
    #Runtime: 1324 ms, faster than 18.81% of Python3 online submissions for 4Sum.
    #Memory Usage: 14.2 MB, less than 82.22% of Python3 online submissions for 4Sum.
    def fourSum(self, nums, target):
        """
        type nums: List[int] \\
        type target: int \\
        type return: List[List[int]] \\
        """
        if len(nums) < 4:
            return []

        def threeSum(num_i, nums, target):
            """
            :type nums: List[int] \\
            :type target: integer \\
            :rtype: List[List[int]]
            """
            if (nums[0] > 0 and target <= 0) or nums[len(nums)-1] < 0 and target >= 0:
                return []
            output = []
            for i in range(len(nums)-2):
                if i>0 and nums[i]==nums[i-1]: #ひとつ前の値と同じときは既に調査済みなので調べない
                    continue
                j = i+1
                k = len(nums)-1
                while j < k:
                    if nums[i]+nums[j]+nums[k] == target:  
                        output.append([num_i,nums[i],nums[j],nums[k]])
                        while j < k-1 and nums[k-1]==nums[k]: #こちらも1つ先の値が同じときは同じものを調べることになるので飛ばす
                            k -=1
                        while j+1 < k and nums[j+1]==nums[j]: #これもそう
                            j +=1    
                        j +=1
                        k -=1
                    elif nums[i]+nums[j]+nums[k] > target: #targetより大きいときはkを1減らして，nums[i]+nums[j]+nums[k]の値を減らす
                        k -=1
                    else: #targetより小さいときはjを1増やして，nums[i]+nums[j]+nums[k]を増加させる
                        j +=1
            return output   

        nums.sort()
        if (nums[0] > 0 and target <= 0) or (nums[len(nums)-1] < 0 and target >= 0):
            print(1)
            return []
        
        output = []
        for i in range(len(nums)-3):
            if i>0 and nums[i-1] == nums[i]:
                continue
            output += threeSum(nums[i], nums[i+1:], target-nums[i])

        return output
    
def main():
    nums = [1,0,-1,0,-2,2]
    target = 0
    sol = Solution2()
    print(sol.fourSum(nums, target))

if __name__ == "__main__":
    main()