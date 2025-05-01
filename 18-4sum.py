# LeetCode Problem 18: 4Sum  
# Problem: https://leetcode.com/problems/4sum/  
# Approach: Two-pointer + nested loops on sorted array  
# Time: O(n^3), Space: O(1) or O(n^2) with result storage

class Solution():
    def fourSum(self, nums, target):
        results = []
        nums.sort()
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            
            for k in range(i+1, len(nums)):
                left= k+1
                right= len(nums) -1
                total_target= target - nums[i] - nums[k] 

                while left < right:
                    total = nums[left] + nums[right]

                    if total == total_target:
                        array= [nums[i],nums[k],nums[left],nums[right]]
                        if array not in results:
                            results.append(array)

                        left+=1
                        right-=1
                    elif total > total_target:
                        right-=1
                    else:
                         left+=1
            
        return results
