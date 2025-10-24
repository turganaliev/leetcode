class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not len(s) == len(t):
            return False
        
        res = [0] * 26

        for letter in s:
            res[ord(letter) - ord("a")] += 1
        
        for letter in t:
            res[ord(letter) - ord("a")] -= 1
        
        for i in res:
            if i != 0:
                return False
        
        return True
    
if __name__=="__main__":
    s = input()
    t = input()
    solution = Solution()
    res = solution.isAnagram(s, t)
    print(res)