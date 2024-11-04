class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        start = 0
        end = len(nums) - 1  # Fixed typo here

        while start<=end:
            mid = start + (end - start) // 2
            mid_value = nums[mid]

            if mid_value == target:
                return mid
            elif mid_value > target:
                end = mid - 1
            else :
                start = mid + 1
        return -1