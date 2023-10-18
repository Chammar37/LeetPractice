class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n

        prefixProd = 1
        suffixProd = 1

        for i in range(n):
            result[i] = prefixProd
            prefixProd *= nums[i]

        for j in range(n-1, -1, -1):
            result[j] *= suffixProd
            suffixProd *= nums[j]
        
        
        return result