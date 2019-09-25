class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = {}
        longest = 0
        left = 0
        right = 0
        for i in range(len(s)):
            if right - left > longest:
                longest = right - left
            x = s[i]
            # 1st, makes sure it's seen before
            # 2nd, makes sure it's within the window defined by left and right
            if x in hashmap and hashmap[x] >= left:
                left = hashmap[x] + 1
            hashmap[x] = i
            right += 1
        if right - left > longest:
            longest = right - left
        return longest
