import random

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def partition(arr, low, high):
            rand_idx = random.randint(low, high)
            arr[rand_idx], arr[high] = arr[high], arr[rand_idx]

            pivot = arr[high]
            i = low - 1

            for j in range(low, high):
                if arr[j] <= pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
            arr[i+1] , arr[high] = arr[high], arr[i+1]
            return i+1
        
        def quick_sort(arr, low, high):

            if low < high:
                pivot_index = partition(arr, low, high)
                quick_sort(arr, low, pivot_index - 1)
                quick_sort(arr, pivot_index + 1, high)
        
        quick_sort(nums, 0, len(nums) - 1)
        return nums
            

        