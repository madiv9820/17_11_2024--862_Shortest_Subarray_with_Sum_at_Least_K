from typing import List
from collections import deque

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        # Initialize the shortest subarray length to infinity (representing no valid subarray found)
        shortest_Subarray_Length = float('inf')
        
        # Get the size of the input array
        n = len(nums)
        
        # Initialize prefix sum (sum of elements up to the current index)
        prefix_sum = 0
        
        # Create a deque to store the prefix sums and their indices
        # The deque stores tuples (prefix_sum, index)
        queue = deque()
        
        # Append the initial tuple (0, -1) to the deque.
        # This represents the sum of elements before the array starts (prefix sum of 0 at index -1).
        queue.append((prefix_sum, -1))

        # Loop through each element in the array to calculate prefix sums
        for index in range(n):
            # Update the current prefix sum by adding the current element
            prefix_sum += nums[index]
            
            # Check if the difference between the current prefix sum and the earliest prefix sum in the deque
            # is greater than or equal to k. This means we have found a subarray with sum >= k.
            while len(queue) and prefix_sum - queue[0][0] >= k:
                # Update the shortest subarray length by comparing it with the current subarray length
                shortest_Subarray_Length = min(shortest_Subarray_Length, index - queue[0][1])
                
                # Remove the front element of the deque since it's no longer needed
                queue.popleft()
            
            # While the deque is not empty and the current prefix sum is less than the prefix sum at the back of the deque,
            # remove elements from the back of the deque. This ensures the deque is always ordered in increasing prefix sums.
            while len(queue) and prefix_sum < queue[-1][0]:
                queue.pop()
            
            # Append the current prefix sum and its index to the deque
            queue.append((prefix_sum, index))

        # If no valid subarray was found, return -1
        if shortest_Subarray_Length == float('inf'):
            shortest_Subarray_Length = -1
        
        # Return the length of the shortest subarray with sum >= k
        return shortest_Subarray_Length