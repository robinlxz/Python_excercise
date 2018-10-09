#Leet code "Easy"
#https://leetcode.com/problems/two-sum/description/

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sort_num = nums
        #print nums
        #sort_num.sort()
        #print nums
        mid = int(len(nums)/2)
        
        for p in range(0,len(sort_num)):            
            q = mid
            while (q > -1) and (q < len(sort_num)):
                if sort_num[p] + sort_num[q] > target:
                    q -= 1
                elif sort_num[p] + sort_num[q] < target:
                    q += 1
                else:
                    #Then need to find the indice for the digit
                    print sort_num[p], sort_num[q]
                    print nums
                    answer = [nums.index(sort_num[p]),nums.index(sort_num[q])]
                    return (answer)
            

A = Solution()
print A.twoSum([1,4,3,2],5)        
