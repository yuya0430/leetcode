class Solution:
    #Runtime: 104 ms, faster than 92.78% of Python3 online submissions for 3Sum Closest.
    #Memory Usage: 14.3 MB, less than 72.70% of Python3 online submissions for 3Sum Closest.
    def threeSumClosest(self, nums, target):
        """
        type nums: List[int]
        type target: int
        type return: int
        """
        nums.sort()
        output = nums[0] + nums[1] + nums[len(nums)-1]
        for i in range(len(nums) - 2):
            if i>0 and nums[i] == nums[i-1]: #一つ前が同じ値の時は調べない
                continue

            if target < 0 and nums[i] > 0:
                break

            j = i + 1
            k = len(nums) - 1
            while j < k:
                sum3 = nums[i] + nums[j] + nums[k]
                print(sum3)
                print("{},{},{}".format(i, j, k))
                input()
                if abs(target - sum3) < abs(target - output):
                    output = sum3
                
                    if output == target:
                        return output
                
                if target < sum3:
                    while j < k-1 and nums[k-1]==nums[k]: #こちらも1つ先の値が同じときは同じものを調べることになるので飛ばす
                        k -=1
                    k -= 1
                else:
                    while j+1 < k and nums[j+1]==nums[j]: #これもそう
                        j +=1  
                    j += 1
        
        return output

def check(nums, target):
    """
        type nums: List[int] \\
        type target: int \\
        leetcodeで不正解だったときに，答えがどのインデックスでの和なのか確認するために使用
    """
    for i in range(len(nums)):
        for j in range(len(nums) - i - 1):
            for k in range(len(nums) - j - 2):
                if nums[i] + nums[j+i+1] + nums[k+j+2] == target:
                    print("{},{},{}".format(i, j+i+1, k+j+2))


def main():
    nums = [13,2,0,-14,-20,19,8,-5,-13,-3,20,15,20,5,13,14,-17,-7,12,-6,0,20,-19,-1,-15,-2,8,-2,-9,13,0,-3,-18,-9,-9,-19,17,-14,-19,-4,-16,2,0,9,5,-7,-4,20,18,9,0,12,-1,10,-17,-11,16,-13,-14,-3,0,2,-18,2,8,20,-15,3,-13,-12,-2,-19,11,11,-10,1,1,-10,-2,12,0,17,-19,-7,8,-19,-17,5,-5,-10,8,0,-12,4,19,2,0,12,14,-9,15,7,0,-16,-5,16,-12,0,2,-16,14,18,12,13,5,0,5,6]
    target = -59
    sol = Solution()
    #check(nums, -58)
    output = sol.threeSumClosest(nums, target)
    print(output)

if __name__ == "__main__":
    main()