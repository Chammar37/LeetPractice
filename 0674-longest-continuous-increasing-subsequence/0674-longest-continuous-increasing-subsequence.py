class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        n = len(nums)
        count = [1] * n 
        countIndex = 0
        curr = nums[0]

        for i in range(n):
            if(nums[i] > curr):
                count[countIndex] += 1
                curr = nums[i]
            else:
                countIndex += 1
                curr = nums[i]
            # print(nums[i],"count",count)

        return max(count)