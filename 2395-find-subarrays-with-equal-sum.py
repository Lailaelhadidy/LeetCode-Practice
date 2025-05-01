# LeetCode Problem 2395: Find Subarrays With Equal Sum  
# Problem: https://leetcode.com/problems/find-subarrays-with-equal-sum/  
# Approach: HashSet to store subarray sums of length 2  
# Time: O(n), Space: O(n)

class Solution(object):
    def findSubarrays(self, nums):
        sum=0
        sums= set()
        for i in range (0, len(nums)-1):
            sum= nums[i] + nums[i+1]
            if sum in sums:
                return True 
            sums.add(sum)
        return False
