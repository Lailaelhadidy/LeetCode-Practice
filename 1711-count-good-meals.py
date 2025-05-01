# LeetCode Problem 1711: Count Good Meals  
# Problem: https://leetcode.com/problems/count-good-meals/  
# Approach: Hashmap with modular arithmetic to count complements  
# Time: O(n * log(max_val)), Space: O(n)

class Solution(object):
    def countPairs(self, deliciousness):
        num_of_meals = 0
        meals = {}

        for i in deliciousness:
            meals[i] = meals.get(i,0) + 1
        
        for i in meals:
            for k in range(22):
                diff = (2**k) - i
                if diff == i:
                    num_of_meals += meals[i] * (meals[i]-1) //2
                elif diff >= i and diff in meals :
                    num_of_meals += meals[i] * meals[diff]
        return num_of_meals % ((10**9) + 7)

