class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        contains = {}
        ans =[]

        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in contains:
                return [contains.get(difference), i]
            contains[nums[i]] = i
        return ans