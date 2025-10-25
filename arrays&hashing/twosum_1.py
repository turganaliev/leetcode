from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i


if __name__=="__main__":
    input_nums = input()
    nums = []
    target = int(input())
    for n in input_nums:
        nums.append(int(n))
    solution = Solution()
    res = solution.twoSum(nums, target)
    print(res)