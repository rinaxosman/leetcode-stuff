from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_index={}

        # for i, num in enumerate(nums):
        #     complement=target-num
        #     if complement in num_index:
        #         return[num_index[complement],i]
        #     num_index[num]=i

        for i in range(len(nums)):  # Using a standard for loop with range
            num = nums[i]  # Access the value at index i
            complement = target - num
            if complement in num_index:
                return [num_index[complement], i]
            num_index[num] = i

if __name__ == "__main__":
    solution = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    print(solution.twoSum(nums, target))  # Expected output: [0, 1]
