# LeetCode Problem 2269: Find the K-Beauty of a Number  
# Problem: https://leetcode.com/problems/find-the-k-beauty-of-a-number/  
# Approach: Sliding window over stringified integer  
# Time: O(n * k), Space: O(1)

class Solution():
    def divisorSubstrings(self, num, k):
        count=0
        s = str(num)
        for i in range(len(s)-k+1):
            set= s[i:i+k]
            if int(set) !=0 and num % int(set) ==0 :
                count+=1
        return count
        
