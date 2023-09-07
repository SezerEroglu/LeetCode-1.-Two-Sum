# LeetCode-1.-Two-Sum

## Keeping track of all differences while first pass

We loop through all values in nums. In all passes, the check if the required diff is found in the differences dictionary. If yes, we return the current index with the index found in the difference dictionary. If not, we add the diff to the dict unless it already exists. In the second pass' second index the dict is complete for every value in the nums array.

Time: O(n) Space: =(n)