class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # for i in range (len(nums)):
        #     for j in range (i+1,len(nums)):
        #         if nums[i] >= nums[j]:
        #             continue
        #         for k in range(len(nums)-1,len(nums)):
        #             if nums[i] < nums[j] < nums[k] and i < j < k :
        #                 return True
        # return False
        first = float('inf')
        second = float('inf')
    
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
            
        return False