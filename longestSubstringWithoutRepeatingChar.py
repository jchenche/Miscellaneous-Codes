class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Given a string, find the length of the longest substring without repeating characters.
        hashmap = {}
        longest = 0
        left = 0
        for i in range(len(s)):
            right = i
            x = s[i]
            # Check if it's seen before and is within the window defined by left and right
            if x in hashmap and hashmap[x] >= left:
                left = hashmap[x] + 1
            elif right - left  + 1 > longest: # Otherwise check if window size is the longest
                longest = right - left + 1
            hashmap[x] = i
        return longest
