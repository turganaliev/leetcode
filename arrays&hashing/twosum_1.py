from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in prevMap:
                return [i, prevMap[diff]]
            else:
                prevMap[nums[i]] = i

        # for i, n in enumerate(nums):
        #     diff = target - n
        #     if diff in prevMap:
        #         return [prevMap[diff], i]
        #     prevMap[n] = i


if __name__=="__main__":
    input_nums = input()
    nums = input_nums.split(' ')
    numbers = []
    target = int(input())
    for n in nums:
        numbers.append(int(n))
    solution = Solution()
    res = solution.twoSum(numbers, target)
    print(res)