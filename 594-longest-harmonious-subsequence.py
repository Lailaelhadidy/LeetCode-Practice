# LeetCode Problem 594: Longest Harmonious Subsequence  
# Problem: https://leetcode.com/problems/longest-harmonious-subsequence/  
# Approach: Hashmap counting with neighbor check  
# Time: O(n), Space: O(n)

from collections import Counter
class Solution(object):
    def findLHS(self, nums):
        count= Counter(nums)
        lenght=0 
        
        for num in count:
            if num+1 in count:
                lenght= max(lenght, count[num] + count[num+1])
        return lenght
        

        
