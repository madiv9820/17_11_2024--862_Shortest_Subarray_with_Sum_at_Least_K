- ## Approach 2:- Prefix Sum Approach using Monotonic Queue
    - ### Intuition
        We are tasked with finding a contiguous subarray whose sum is greater than or equal to `k`. A brute-force approach would involve checking all possible subarrays, calculating their sums, and tracking the shortest one that meets the condition. However, this would take **O(n^2)** time, which could be too slow for large input sizes.

        Instead, we can use a **sliding window** or **prefix sum** technique along with a **monotonic deque** to improve efficiency. The basic idea is to keep track of the cumulative sum (prefix sum) and use a deque to efficiently find the shortest subarray whose sum meets or exceeds `k`. 

    - ### Approach
        1. **Prefix Sum**:
            - We maintain a running sum, `prefix_sum`, that represents the sum of elements from the start of the array up to the current index.
        2. **Monotonic Deque**:
            - We use a deque (`queue`) to store pairs of `(prefix_sum, index)`. The deque is maintained in such a way that the prefix sums are ordered from smallest to largest.
            - The idea is to always look for a subarray whose sum is at least `k`. If `prefix_sum[i] - prefix_sum[j] >= k` (where `j < i`), it indicates a valid subarray from index `j+1` to `i`.
        3. **Deque Operations**:
            - For each element in the array:
                - **Remove invalid subarrays**: If the difference between the current prefix sum and the prefix sum at the front of the deque is greater than or equal to `k`, it means we have found a subarray with sum at least `k`. We update the shortest length and remove the front element from the deque.
                - **Maintain order in the deque**: Remove elements from the back of the deque if the current prefix sum is smaller than the last element’s prefix sum. This ensures that the deque remains ordered in increasing prefix sums.
                - **Add the current prefix sum and index**: We then push the current `prefix_sum` and its index to the deque.
        4. **Edge Cases**:
            - If no valid subarray is found by the end of the iteration, return `-1`.
            - Handle cases where the array is empty or all values are negative.

    - ### Code Implementation
        - **Python Solution**

            ```python3 []
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
            ```

        - **C++ Solution**

            ```cpp []
            class Solution {
            public:
                int shortestSubarray(vector<int>& nums, int k) {
                    // Initialize the shortest subarray length to a very large value (infinity).
                    int shortest_Subarray_Length = numeric_limits<int>::max();
                    
                    // Get the size of the input array.
                    int n = nums.size();
                    
                    // Initialize the prefix sum variable (sum of elements up to the current index).
                    long long prefix_sum = 0;
                    
                    // Create a deque to store pairs of (prefix_sum, index).
                    // This will help in efficiently finding subarrays whose sum is >= k.
                    deque<pair<long long, int>> queue;
                    
                    // Initially, we add a pair (0, -1) to the deque. This represents the sum before the array starts (prefix sum 0 at index -1).
                    queue.push_back({0, -1});

                    // Iterate through the array to compute the prefix sums.
                    for(int index = 0; index < n; ++index) {
                        // Update the current prefix sum by adding the current element of the array.
                        prefix_sum += nums[index];
                        
                        // Check if there exists a subarray with sum >= k.
                        // If the current prefix sum minus the front element's prefix sum is greater than or equal to k,
                        // we found a valid subarray.
                        while(!queue.empty() && prefix_sum - queue.front().first >= k) {
                            // Update the shortest subarray length by comparing the current length with the previous shortest length.
                            shortest_Subarray_Length = min(shortest_Subarray_Length, index - queue.front().second);
                            
                            // Remove the front element from the deque since it is no longer needed.
                            queue.pop_front();
                        }

                        // Ensure that the deque is ordered by increasing prefix sum.
                        // Remove elements from the back of the deque where the current prefix sum is smaller than the last one.
                        while(!queue.empty() && prefix_sum < queue.back().first) {
                            queue.pop_back();
                        }

                        // Add the current prefix sum and its index to the deque.
                        queue.push_back({prefix_sum, index});
                    }

                    // If no valid subarray was found, return -1.
                    if(shortest_Subarray_Length == numeric_limits<int>::max()) {
                        shortest_Subarray_Length = -1;
                    }
                    
                    // Return the length of the shortest subarray whose sum is >= k.
                    return shortest_Subarray_Length;
                }
            };
            ```

    - ### Time Complexity
        - **Outer loop**: We iterate through each element of the array once.
        - **Deque operations**: Each element is pushed and popped from the deque at most once.
        - Overall, each element is processed in constant time due to efficient deque operations, which gives us a linear time complexity.
        - **Time Complexity:** **O(n)**, where `n` is the length of the input array.

    - ### Space Complexity
        - We use a deque to store pairs of `(prefix_sum, index)`. In the worst case, the deque will store all `n` elements of the array (if all prefix sums are unique).
        - Therefore, the space complexity is determined by the number of elements in the deque.
        - **Space Complexity:** **O(n)**, where `n` is the length of the input array.