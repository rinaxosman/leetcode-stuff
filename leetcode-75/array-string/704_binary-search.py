class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Binary Search Explanation and Intuition:
        We use binary search to find `target` in a sorted list `nums`.
        
        Intuition:
        - Start with two pointers, `start` and `end`, covering the whole list.
        - Calculate the midpoint `mid` and compare `nums[mid]` with `target`.
        - If `nums[mid]` == `target`, return `mid` (target found).
        - If `nums[mid]` > `target`, search in the left half by setting `end = mid - 1`.
        - If `nums[mid]` < `target`, search in the right half by setting `start = mid + 1`.
        - Repeat until `start` exceeds `end`. Return -1 if `target` is not found.

        Time Complexity: O(log n)
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
                
        return -1
