class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        number_count = defaultdict(int)
        majority_element = None
        for num in nums:
            number_count[num] = number_count.get(num, 0) + 1 
        
        for key, value in number_count.items():
            if value > len(nums) // 2 :
                majority_element = key
        
        return majority_element