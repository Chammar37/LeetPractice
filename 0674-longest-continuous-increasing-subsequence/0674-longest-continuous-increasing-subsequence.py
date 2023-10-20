class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        n = len(nums)
        count = 1
        maxCount = 1
        curr = nums[0]

        for i in range(n):
            if(nums[i] > curr):
                count += 1
                curr = nums[i]
                print(count, i)
            else:
                curr = nums[i]
                maxCount = max(count, maxCount)
                count = 1
                print("max",maxCount)
            # print(nums[i],"count",count)

        return max(count, maxCount)