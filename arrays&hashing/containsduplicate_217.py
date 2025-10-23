from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        
        return False
    

if __name__=="__main__":
    input_nums = input()
    nums = []
    for n in input_nums:
        nums.append(int(n))
    solution = Solution()
    res = solution.containsDuplicate(nums)
    print(res)
    