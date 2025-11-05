from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        countMap = {}

        for i in nums:
            countMap[i] = countMap.get(i, 0) + 1

        for key, value in countMap.items():
            if value > len(nums) / 2:
                return key
        
        return -1
            

if __name__ == '__main__':
    n = input()
    nums = []
    for num in n.split():
        nums.append(int(num))
    res = Solution().majorityElement(nums)
    print(res)