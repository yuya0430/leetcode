#提出者の75%に負ける速度をたたき出した．．．
#メモリ使用量は上位20%に入った

class Solution:
    def findMedianSortedArrays(self, nums1: list, nums2: list) -> float:
        if len(nums1) < len(nums2): #長いのをnums1にする
            nums1, nums2 = nums2, nums1

        index = 0
        for n2 in nums2:
            if n2 < nums1[index]: #nums1にある最初の数より小さいときはここでどんどん追加
                nums1.insert(index, n2)
                continue
            while True:
                if len(nums1) == index + 1: #index が最後まで到達したら
                    nums1.append(n2)
                    break
                #---nums1の各要素の間に収まるかを調べて追加---#
                elif nums1[index] <= n2 and n2 < nums1[index + 1]:
                    nums1.insert(index+1, n2)
                    break
                else:
                    index += 1 #間に収まらないときは次に進む

        index = len(nums1) / 2
        if index % 1 == 0: #整数(偶数)の時
            return (nums1[int(index - 1)] + nums1[int(index)])/2
        else: #少数(奇数)の時
            return nums1[int(index)]

def main():
    n1 = [1,2]
    n2 = [-1,3]
    solution = Solution()
    output = solution.findMedianSortedArrays(n1, n2)

    print(output)

if __name__ == "__main__":
    main()