class Solution(object):
    def twoSum(self, nums, target):
        list = [];
        for i in range(0,len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    list.append(i);
                    list.append(j);
                    break;
        return(list);
        