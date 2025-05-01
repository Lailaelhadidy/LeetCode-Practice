# LeetCode Problem 2351: First Letter to Appear Twice  
# Problem: https://leetcode.com/problems/first-letter-to-appear-twice/  
# Approach: Hashset to track visited characters  
# Time: O(n), Space: O(1)

class Solution(object):
    def repeatedCharacter(self, s):
        appeared= []
        for i in s:
            if i in appeared:
                return i
            appeared.append(i)

