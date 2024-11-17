- ## Approach 3:- Prefix Sum Approach using Min Priority Queue
    - ### Intuition
        The problem is to find the length of the shortest contiguous subarray whose sum is at least `k`. The brute-force approach of checking all subarrays would be too slow __(O(n<sup>2</sup>))__ for larger arrays, so we need to optimize the solution. We can use the **prefix sum** technique along with a **priority queue (min-heap)** to efficiently solve the problem.

        - **Prefix sum** allows us to compute the sum of any subarray in constant time. The sum of a subarray from index `i` to `j` is simply the difference between the prefix sums: `prefix_sum[j] - prefix_sum[i-1]`.
        - **Priority queue (min-heap)** is used to store the prefix sums and their corresponding indices in increasing order. This helps us quickly find the shortest subarray whose sum is greater than or equal to `k`.

    - ### Key Idea:
        - As we calculate the prefix sum for each element, we can check the difference between the current prefix sum and previously seen prefix sums stored in the heap.
        - If the difference is greater than or equal to `k`, we have found a subarray whose sum is at least `k`, and we can update the shortest length.

    - ### Approach
        1. **Prefix Sum Calculation**:
            - Maintain a running sum `prefix_sum` as you iterate through the array.    
        2. **Min-Heap to Track Prefix Sums**:
            - Use a priority queue (min-heap) to store pairs of `(prefix_sum, index)`, where `prefix_sum` is the cumulative sum up to that index.
            - Push `(0, -1)` initially to represent the sum before the start of the array, making it easier to compute sums from the start.
        3. **Check Valid Subarrays**:
            - For each element at index `i`, calculate the new `prefix_sum` by adding `nums[i]`.
            - If the difference between the current `prefix_sum` and the smallest `prefix_sum` in the heap is greater than or equal to `k`, it means there is a valid subarray, and we can calculate its length (`i - index`).
            - Keep track of the shortest valid subarray length.
        4. **Update the Heap**:
            - After checking for valid subarrays, push the current `prefix_sum` and its index into the heap for future subarray checks.
        5. **Edge Case**:
            - If no valid subarray is found, return `-1`.

    - ### Code Implementation
        - **Python Solution**

            ```python3 []
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
            ```

        - **C++ Solution**

            ```cpp []
            class Solution {
            public:
                int shortestSubarray(vector<int>& nums, int k) {
                    // Initialize the shortest subarray length to infinity. This means no valid subarray found yet.
                    int shortest_Subarray_Length = numeric_limits<int>::max();
                    
                    // Get the size of the input array
                    int n = nums.size();
                    
                    // Initialize the prefix sum to 0 (cumulative sum of elements up to the current index)
                    long long prefix_sum = 0;
                    
                    // Priority Queue (Min-Heap) to store pairs of (prefix_sum, index).
                    // The priority queue is ordered by the prefix_sum in increasing order.
                    priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>> min_heap;
                    
                    // Push the initial value (0, -1) into the min-heap to represent the sum of elements before the array starts
                    min_heap.push({0, -1});

                    // Iterate through the array to compute prefix sums
                    for (int index = 0; index < n; ++index) {
                        // Update the current prefix sum by adding the current element of the array
                        prefix_sum += nums[index];
                        
                        // Check if there is any prefix sum in the heap such that the difference between current prefix_sum
                        // and the prefix sum in the heap is greater than or equal to k.
                        // If so, we have found a subarray with a sum >= k.
                        while (!min_heap.empty() && prefix_sum - min_heap.top().first >= k) {
                            // Update the shortest subarray length by comparing the current subarray length
                            // with the previously found shortest length.
                            shortest_Subarray_Length = min(shortest_Subarray_Length, index - min_heap.top().second);
                            
                            // Pop the top element from the heap as we don't need it anymore
                            min_heap.pop();
                        }
                        
                        // Push the current prefix_sum and its index into the min-heap
                        min_heap.push({prefix_sum, index});
                    }

                    // If no valid subarray is found, return -1
                    if (shortest_Subarray_Length == numeric_limits<int>::max()) {
                        shortest_Subarray_Length = -1;
                    }
                    
                    // Return the length of the shortest subarray whose sum is >= k
                    return shortest_Subarray_Length;
                }
            };
            ```

    - ### Time Complexity
        - **Heap Operations**: Each element can be pushed and popped from the heap at most once. Each heap operation (push/pop) takes O(log n) time.
        - **Iterating Through the Array**: We loop through all `n` elements.
        - Therefore, the overall time complexity is **O(n log n)** due to the heap operations.

    - ### Space Complexity
        - **Heap Storage**: In the worst case, the heap stores all `n` elements. Each element is a pair of `(prefix_sum, index)`, which takes constant space.   
        - Thus, the space complexity is **O(n)**, as the heap can store at most `n` elements.