from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0

        count = 0
        for i in nums:
            if i != val:
                nums[count] = i
                count += 1
        return count
    

if __name__ == '__main__':
    n = input()
    nums = []
    for i in n.split():
        nums.append(int(i))
    target = int(input())
    solution = Solution()
    res = solution.removeElement(nums, target)
    print(res)