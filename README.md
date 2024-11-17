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

        **Time Complexity:**  **O(n<sup>2</sup>)** where `n` is the size of the input array.

    - ### Space Complexity
        - The solution does not use any additional data structures that scale with the input size.
        - We only use a few variables (e.g., for tracking the sum and shortest length), so the space complexity is constant.
        
        **Space Complexity:** **O(1)** (constant space).