#https://leetcode.com/problems/two-sum/

#lxz review 20190218
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        buff_dict = {}
        for i in range(len(nums)):
            if target - nums[i] in buff_dict:
                return (buff_dict[target - nums[i]], i)
            else:
                buff_dict[nums[i]] = i
                #print buff_dict

A = Solution()
print A.twoSum([2, 11, 15, 7], 9)