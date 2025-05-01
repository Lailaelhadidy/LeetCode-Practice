# LeetCode Problem 187: Repeated DNA Sequences  
# Problem: https://leetcode.com/problems/repeated-dna-sequences/  
# Approach: Hashset for seen and added substrings of size 10  
# Time: O(n), Space: O(n)

class Solution():
    def findRepeatedDnaSequences(self, s):
        overall_added= set()
        added= set()

        for i in range(len(s)):
            new= s[i: i+10]
            if new in added:
                overall_added.add(new)
            added.add(new)

        return list(overall_added)
        


        
