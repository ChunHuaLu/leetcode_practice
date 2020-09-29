# leetcode 348 with list
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        bucket_26 = [0]*26
        ana_t = [0]*26
        for i in range(0, len(p)):
            ana_t[ord(p[i]) - ord('a')] += 1
        start = 0
        for j in range(0, len(s)):
            bucket_26[ ord(s[j]) - ord("a") ] += 1
            if j >= len(p):
                bucket_26[ ord(s[start]) - ord('a') ] -= 1
                start += 1
            if bucket_26 == ana_t:
                result.append(start)
        return result