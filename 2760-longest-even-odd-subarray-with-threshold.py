# LeetCode Problem 2760: Longest Even Odd Subarray With Threshold  
# Problem: https://leetcode.com/problems/longest-even-odd-subarray-with-threshold/  
# Approach: Sliding window to track alternating even-odd sequence under threshold  
# Time: O(n), Space: O(1)

class Solution():
    def longestAlternatingSubarray(self, nums, threshold):
        maximum_length=0

        for i in range(len(nums)):
            if nums[i] % 2 == 0 and nums[i] <= threshold:
                length=1

                if length>maximum_length:
                    maximum_length= length
                    
                for k in range(i+1, len(nums)):
                    if nums[k] % 2 != nums[k-1] %2 and nums[k] <= threshold:
                        length+=1
                    else:
                        break
                maximum_length = max(maximum_length, length)

        return maximum_length


        
