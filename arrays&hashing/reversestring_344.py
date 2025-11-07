from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        first = 0
        last = len(s) - 1

        for string in range(len(s) // 2):
            temp = s[first]
            s[first] = s[last]
            s[last] = temp
            first += 1
            last -= 1

        return s
    

if __name__ == '__main__':
    s = input()
    s_list = s.split()
    print(s_list)
    res = Solution().reverseString(s_list)
    print(res)