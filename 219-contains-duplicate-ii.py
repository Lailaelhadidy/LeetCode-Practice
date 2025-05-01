# LeetCode Problem 219: Contains Duplicate II  
# Problem: https://leetcode.com/problems/contains-duplicate-ii/  
# Approach: Sliding window using HashMap to track indices  
# Time: O(n), Space: O(n)

class Solution:
    def containsNearbyDuplicate(self, nums, k):
        saved_index = {}
        for i in range(len(nums)):
            if nums[i] in saved_index and abs(i - saved_index[nums[i]]) <= k:
                return True
            saved_index[nums[i]] = i
        return False
