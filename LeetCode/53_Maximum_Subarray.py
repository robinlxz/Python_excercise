#https://leetcode.com/problems/maximum-subarray/

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        biggest = nums[0]
        # Take all possible amount of numbers i
        for i in range(1, len(nums)+1):
            # Find sum of each combination for i numbers
            for p in range(0, len(nums) - i + 1):
                if biggest < sum(nums[p:(p + i)]):
                #if 1<2:
                    biggest = sum(nums[p:(p + i)])
                    res = nums[p:(p + i)]
                    #print 'now biggest is', biggest
                    #print 'res is', res
                    #print nums[p:(p + i)]
        #return max(sum)
        return biggest


class Solution2(object):
    #https://leetcode.com/problems/maximum-subarray/discuss/20396/Easy-Python-Way
    #https://afshinm.name/2018/06/24/why-kadane-algorithm-works/
    def maxSubArray(selfself, nums):
        for i in range(1, len(nums)):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]
            print nums
        return max(nums)

#lxz review (Kadane Algorithm)
class Solution3(object):
    def maxSubArray(selfself, nums):
        curMax = allMax = nums[0]
        for x in nums:
            curMax = max(x, x+curMax)
            allMax = max(curMax, allMax)
        return allMax


A = Solution3()
print A.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
#print A.maxSubArray([-2,1,-3,4])
exit()
