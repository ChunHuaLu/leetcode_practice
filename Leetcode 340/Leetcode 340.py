# leetcode 340. Longest Substring with at most k distinct characters
from collections import deque

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        # hashmap
        tmp_set = set(s)
        tmp_dict = dict()
        for j in tmp_set:
            tmp_dict[j] = 0
        start = 0
        # queue
        tmp_str = deque()
        max_len = 0
        cnt = 0
        for i in range(0, len(s)):
            if cnt <= k:
                max_len = max(max_len, len(tmp_str))
                tmp_str.append(s[i])
                if tmp_dict[s[i]] == 0:
                    cnt += 1
                tmp_dict[s[i]] += 1
                # move start window
                while cnt > k:
                    tmp_char = tmp_str.popleft()
                    tmp_dict[tmp_char] -= 1
                    if tmp_dict[tmp_char] == 0:
                        cnt -= 1
        if cnt <= k:
            max_len = max(max_len, len(tmp_str))
        return max_len


