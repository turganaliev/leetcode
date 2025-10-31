from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(len(strs[0])):
            for word in strs:
                if i == len(word) or word[i] != strs[0][i]:
                    return word[:i]
        
        return strs[0]
    

if __name__=="__main__":
    print("Please, type your words separated by space: ")
    words = input()
    words_list = words.split()

    solution = Solution()
    res = solution.longestCommonPrefix(words_list)
    print(res)