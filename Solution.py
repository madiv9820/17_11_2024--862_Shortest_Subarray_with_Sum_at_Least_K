from typing import List
import sys

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        # Initialize the shortest subarray length to a large value (infinity)
        shortest_Subarray_Length = sys.maxsize
        # Get the length of the input array
        n = len(nums)

        # Outer loop to iterate over the starting index of the subarray
        for index in range(n):
            # Initialize subarray sum for the current starting index
            subarray_Sum = 0
            # Inner loop to explore subarrays starting from the 'index' position
            for currentIndex in range(index, n):
                # Add the current element to the subarray sum
                subarray_Sum += nums[currentIndex]
                # Check if the current subarray sum meets or exceeds the target k
                if subarray_Sum >= k:
                    # Update the shortest subarray length if a smaller subarray is found
                    shortest_Subarray_Length = min(shortest_Subarray_Length, currentIndex - index + 1)
                    # No need to check further subarrays starting at 'index', break out of the inner loop
                    break

        # If no valid subarray was found, return -1
        if shortest_Subarray_Length == sys.maxsize:
            shortest_Subarray_Length = -1
        
        # Return the length of the shortest subarray with a sum >= k
        return shortest_Subarray_Length