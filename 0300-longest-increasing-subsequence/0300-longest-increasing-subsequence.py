class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # n = len(nums)
        # count = 1
        # maxCount = 1
        
        # #My Method:
        # #for each element in the array, look for nearest 
        # #largest element , do this recursively until reaching end of array. O(n^2)

        # for i in range(n):
        #     last = nums[i]
        #     for j in range(i, n):
        #         if nums[j] > last:
        #             last = nums[j]
        #             count += 1
        #             # print("element:", last)
        #             # print("in loop", count)
        #         else:
        #             continue
        #     maxCount = max(count, maxCount)
        #     print("max: ", maxCount)
        #     count = 1
                
        # return maxCount


        #### STARTING AT 0 SOLUTION ####
        # if not nums:
        # return 0

        # n = len(nums)
        # dp = [1] * n

        # for i in range(n):
        #     for j in range(i):
        #         if nums[i] > nums[j]:
        #             dp[i] = max(dp[i], dp[j] + 1)

        # return max(dp)


        #### REVERSE ORDER SOLUTION. FINDING SUBSEQUENCES AT EVERY INDEX, IN REVERSE. CACHING ANSWER ####
        
        n = len(nums)
        LIS = [1] * n

        for i in range(n, -1 , -1):
            for j in range (i+1, n):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        return max(LIS)