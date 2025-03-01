from typing import List

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # First pass: Apply operations (double and set next to zero)
        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0

        # Second pass: Move non-zero elements to the front
        j = 0  # Position to place non-zero elements
        for i in range(n):
            if nums[i] != 0:
                nums[j], nums[i] = nums[i], nums[j]  # Swap non-zero element forward
                j += 1

        return nums
