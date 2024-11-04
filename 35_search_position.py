class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        Explanation and Intuition:
        This function performs a binary search to find the position of `target` in a sorted list `nums`.
        
        Intuition:
        - Start with two pointers, `start` at the beginning and `end` at the end of `nums`.
        - Calculate the midpoint `mid` and compare `nums[mid]` with `target`.
        - If `nums[mid]` == `target`, return `mid` (we found the exact position).
        - If `nums[mid]` > `target`, set `end = mid - 1` to search the left half (since `target` must be in the lower half).
        - If `nums[mid]` < `target`, set `start = mid + 1` to search the right half (since `target` must be in the upper half).
        - If `start` exceeds `end`, `start` will be the insertion position where `target` would fit in sorted order.

        The binary search allows us to find the exact or insertion position efficiently with O(log n) complexity.
        """
        
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = start + (end - start) // 2
            mid_value = nums[mid]

            if mid_value == target:
                return mid
            elif mid_value > target:
                end = mid - 1
            else:
                start = mid + 1
            
        # When the loop ends, `start` is the insertion index for `target`
        return start
