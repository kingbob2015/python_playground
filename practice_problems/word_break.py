# Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

# Note:

# The same word in the dictionary may be reused multiple times in the segmentation.
# You may assume the dictionary does not contain duplicate words.
# Example 1:

# Input: s = "leetcode", wordDict = ["leet", "code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".
# Example 2:

# Input: s = "applepenapple", wordDict = ["apple", "pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
#              Note that you are allowed to reuse a dictionary word.
# Example 3:

# Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output: false

from collections import deque

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        q = deque()
        q.append(s)
        while len(q) > 0:
            workingString = q.popleft()
            for w in wordDict:
                if w == workingString:
                    return True
                elif len(w) < len(workingString):
                    if w == workingString[:len(w)]:
                        q.append(workingString[len(w):])
        return False
        
#         if len(wordDict) == 0:
#             return False
#         wordDict = set(wordDict)
#         minWordLen = min(map(len, wordDict))
#         sWordEnds = []
#         for i in range(minWordLen-1, len(s)):
#             if s[:i+1] in wordDict:
#                 sWordEnds.append(i)
#             else:
#                 for j in sWordEnds:
#                     if s[j+1:i+1] in wordDict:
#                         sWordEnds.append(i)
#         if len(sWordEnds) == 0:
#             return False
#         else:
#             return sWordEnds[-1] == len(s)-1