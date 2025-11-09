class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = "".join(ch for ch in s if ch.isalnum()).lower()
        # return clean_s == clean_s[::-1]

        left = 0
        right = len(clean_s) - 1
        for ch in range(len(clean_s) // 2):
            if clean_s[left] != clean_s[right]:
                return False
            left += 1
            right -= 1
        
        return True
    

if __name__ == '__main__':
    s = input()
    res = Solution().isPalindrome(s)
    print(res)