class Solution:
    def threeSum(self, nums): #他人の解答（イテレーターを上手いこと動かせばいい説）
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        list_ = []
        nums = sorted(nums)
        if len(nums)<3 or nums[0]>0: #リストの長さが2以下，リストが正の値のみのとき
            return list_
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]: #ひとつ前の値と同じときは既に調査済みなので調べない
                continue
            j = i+1
            k = len(nums)-1
            while j < k:
                if nums[j]+nums[k] == -nums[i]:  
                    list_.append([nums[i],nums[j],nums[k]])
                    while j < k-1 and nums[k-1]==nums[k]: #こちらも1つ先の値が同じときは同じものを調べることになるので飛ばす
                        k -=1
                    while j+1 < k and nums[j+1]==nums[j]: #これもそう
                        j +=1    
                    j +=1
                    k -=1
                elif nums[j]+nums[k] > -nums[i]: #nums[i]より大きいときはkを1減らして，nums[j]+nums[k]を減らす
                    k -=1
                else: #nums[i]より小さいときはjを1増やして，nums[j]+nums[k]を増加させる
                    j +=1
        return list_      
    
    def threeSum3(self, nums): # 失敗
        """
        type nums: List[int] \\
        type return: List[List[int]] \\
        """

        if len(nums) < 3:
            return []

        def Two_Sum(nums):
            two_sum_hash = {}
            for i in range(len(nums)):
                for j in range(len(nums)-i-1):
                    two_sum = nums[i] + nums[j+i+1]
                    if two_sum not in two_sum_hash:
                        two_sum_hash[two_sum] = [({"num":nums[i],"idx":i}, {"num":nums[j+i+1], "idx":j+i+1})]
                    else:
                        if [nums[i], nums[j+i+1]] not in two_sum_hash[two_sum]:
                            two_sum_hash[two_sum].append(({"num":nums[i],"idx":i}, {"num":nums[j+i+1], "idx":j+i+1}))

            return two_sum_hash

        
        nums.sort()
        two_sum_hash = Two_Sum(nums)
        
        output = []
        for two_sum, two_num_list in two_sum_hash.items():
            if two_sum*-1 in nums:
                for two_num_tupple in two_num_list:
                    tmp = nums.copy()
                    print(tmp)
                    print(two_num_tupple[1]["idx"])
                    tmp.pop(two_num_tupple[1]["idx"])
                    tmp.pop(two_num_tupple[0]["idx"])
                    append_list = [two_num_tupple[0]["num"], two_num_tupple[1]["num"], two_sum*-1]
                    append_list.sort()
                    if two_sum*-1 in tmp and append_list not in output:
                        output.append(append_list) 
        
        return output

    def threeSum2(self, nums): #失敗
        """
        type nums: List[int] \\
        type return: List[List[int]] \\
        """

        if len(nums) < 3:
            return []

        def minus_plus_separate(nums):
            nums.sort()
            try:
                index = nums.index(0)
                return nums[:index], nums[index:]
            except ValueError:
                index = len(nums) // 2
                while True:
                    if nums[index] > 0:
                        if index == 0 or nums[index-1] < 0:
                            return nums[:index], nums[index:]
                        index -= 1
                    else:
                        if index == len(nums)-1 or nums[index+1] > 0:
                            return nums[:index+1], nums[index+1:]
                        index += 1

        def search_sum0(nums1, nums2, output):
            if len(nums1) < 2:
                return output
            
            for i in range(len(nums1)):
                for j in range(len(nums1[i+1:])):
                    two_sum = nums1[i] + nums1[j + i + 1]
                    if two_sum * -1 in nums2 and [nums1[i], nums1[j+i+1], two_sum * -1] not in output:
                        output.append([nums1[i], nums1[j+i+1], two_sum * -1])
        
            return output


                    
        minus_nums, plus_nums = minus_plus_separate(nums)
        output = []
        if plus_nums.count(0) >= 3:
            output.append([0,0,0])
        
        output = search_sum0(minus_nums, plus_nums, output)
        output = search_sum0(plus_nums, minus_nums, output)

        return output

def main():
    nums = [-55,-24,-18,-11,-7,-3,4,5,6,9,11,23,33]
    sol = Solution()
    output = sol.threeSum(nums)
    print(output)

if __name__ == "__main__":
    main()