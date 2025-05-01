# LeetCode Problem 2023: Number of Pairs of Strings With Concatenation Equal to Target  
# Problem: https://leetcode.com/problems/number-of-pairs-of-strings-with-concatenation-equal-to-target/  
# Approach: Brute-force double loop with string concatenation  
# Time: O(n^2 * m), Space: O(1)

class Solution(object):
    def numOfPairs(self, nums, target):
        count=0
        for i in range(0,len(nums)):
            for k in range(0, len(nums)):
                if i!=k and nums[i] + nums[k] == target:
                    count+=1

        return count        
        
