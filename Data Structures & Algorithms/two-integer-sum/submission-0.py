class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen: dict[int,int] = {} 
        for i, num in enumerate(nums):
            aim = target - num
            if aim in seen:
                return [seen[aim], i]
            seen[num] = i
            