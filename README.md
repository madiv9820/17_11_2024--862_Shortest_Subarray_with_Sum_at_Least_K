# Shortest Subarray with Sum at Least K (All Approaches)
- ## Problem Understanding: 
    - Given an integer array `nums` and an integer `k`, the goal is to find the length of the shortest subarray whose sum is at least `k`. If no such subarray exists, return `-1`.

- ## Approach 1:- Brute Force using Nested Loops (Time Limit Exceed)

    - ### Intuition
        The goal is to find the shortest contiguous subarray whose sum is greater than or equal to `k`. A brute force approach would involve checking every possible subarray, calculating their sums, and tracking the minimum length that meets the condition. However, this would have a time complexity of __O(n<sup>2</sup>)__, which could be inefficient for large arrays.

    - ### Approach
        1. **Outer Loop (Starting Index)**:
            - Iterate through each possible starting index `i` of the subarray.
        2. **Inner Loop (Sum Accumulation)**:
            - For each starting index `i`, iterate over the array elements and maintain a running sum of the subarray.
            - If the sum of the subarray becomes greater than or equal to `k`, check if this subarray is shorter than any previously found subarrays with sum >= `k`. If so, update the shortest length.
        3. **Break Early**:
            - As soon as we find a valid subarray (with sum >= `k`), we break out of the inner loop and move to the next starting index. This avoids unnecessary checks for larger subarrays starting at the same index.
        4. **Final Check**:
            - If no subarray meeting the condition was found, return `-1`.
        5. **Edge Cases**:
            - If the array has only one element, check if it is greater than or equal to `k`.
            - If all elements are negative and `k` is positive, no valid subarray can exist.

    - ### Code Implementation
        - **Python Solution**

            ```python3 []
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
            ```
        
        - **C++ Solution**

            ```cpp []
            class Solution {
            public:
                int shortestSubarray(vector<int>& nums, int k) {
                    // Initialize the shortest subarray length to the maximum possible value (infinity)
                    int shortest_Subarray_Length = numeric_limits<int>::max();
                    // Get the size of the input array
                    int n = nums.size();

                    // Outer loop to iterate over the starting index of the subarray
                    for(int index = 0; index < n; ++index) {
                        // Initialize the sum of the subarray for the current starting index
                        int subarray_Sum = 0;
                        
                        // Inner loop to iterate over the current subarray starting at 'index'
                        for(int currentIndex = index; currentIndex < n; ++currentIndex) {
                            // Add the current element to the subarray sum
                            subarray_Sum += nums[currentIndex];
                            
                            // If the sum of the subarray meets or exceeds k
                            if(subarray_Sum >= k) {
                                // Update the shortest subarray length found so far, if the current subarray is smaller
                                shortest_Subarray_Length = min(shortest_Subarray_Length, currentIndex - index + 1);
                                // Since we found a valid subarray, break out of the inner loop to start checking the next starting index
                                break;
                            }
                        }
                    }

                    // If no subarray was found that satisfies the condition, return -1
                    if(shortest_Subarray_Length == numeric_limits<int>::max()) {
                        shortest_Subarray_Length = -1;
                    }

                    // Return the length of the shortest subarray with sum >= k
                    return shortest_Subarray_Length;
                }
            };
            ```

    - ### Time Complexity
        - **Outer loop**: Runs `n` times, where `n` is the length of the array.
        - **Inner loop**: For each starting index, the inner loop runs up to `n - i` times, where `i` is the current index in the outer loop.
        - **Worst-case time complexity**: The total number of iterations is O(n^2), because for each element in the array, we may potentially iterate over all remaining elements.
        - **Time Complexity:**  **O(n<sup>2</sup>)** where `n` is the size of the input array.

    - ### Space Complexity
        - The solution does not use any additional data structures that scale with the input size.
        - We only use a few variables (e.g., for tracking the sum and shortest length), so the space complexity is constant.
        - **Space Complexity:** **O(1)** (constant space).

- ## Approach 2:- Prefix Sum Approach using Monotonic Queue
    - ### Intuition
        We are tasked with finding a contiguous subarray whose sum is greater than or equal to `k`. A brute-force approach would involve checking all possible subarrays, calculating their sums, and tracking the shortest one that meets the condition. However, this would take **O(n<sup>2</sup>)** time, which could be too slow for large input sizes.

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