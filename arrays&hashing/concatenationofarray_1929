from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums)

        for i in range(2):
            for num in nums:
                ans.append(num)
            
        return ans


if __name__=="__main__":
    input_nums = input()
    nums = []
    for n in input_nums:
        nums.append(int(n))
    solution = Solution()
    res = solution.getConcatenation(nums)
    print(res)