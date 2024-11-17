from typing import List
import heapq

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        # Initialize the shortest subarray length to infinity, which means no valid subarray found yet
        shortest_Subarray_Length = float('inf')
        
        # Get the size of the input array
        n = len(nums)
        
        # Initialize the prefix sum to 0 (sum of elements up to the current index)
        prefix_sum = 0
        
        # Initialize a min-heap (priority queue). The heap stores pairs (prefix_sum, index).
        # We start by adding the initial tuple (0, -1), which represents the prefix sum before the start of the array.
        min_heap = [(0, -1)]
        heapq.heapify(min_heap)  # Convert the list to a valid heap.

        # Iterate through the array to calculate the prefix sums
        for index in range(n):
            # Update the current prefix sum by adding the current element of the array
            prefix_sum += nums[index]
            
            # While the heap is not empty, we will check if we can find a valid subarray
            while len(min_heap) > 0:
                # Pop the smallest element from the heap. This gives us the smallest prefix sum seen so far
                # and the index where that prefix sum occurred.
                sum_Till_Index, Index = heapq.heappop(min_heap)
                
                # Check if the current subarray sum is >= k (prefix_sum - sum_Till_Index >= k)
                if prefix_sum - sum_Till_Index >= k:
                    # If the condition is met, calculate the length of the current subarray (index - Index)
                    shortest_Subarray_Length = min(shortest_Subarray_Length, index - Index)
                else:
                    # If the subarray does not meet the condition, we push the element back into the heap
                    # and break the loop because we no longer need to check for earlier sums.
                    heapq.heappush(min_heap, (sum_Till_Index, Index))
                    break
            
            # After checking the subarray, push the current prefix sum and its index into the heap
            heapq.heappush(min_heap, (prefix_sum, index))
        
        # If no valid subarray was found, return -1
        if shortest_Subarray_Length == float('inf'):
            shortest_Subarray_Length = -1
            
        # Return the length of the shortest subarray with sum >= k
        return shortest_Subarray_Length