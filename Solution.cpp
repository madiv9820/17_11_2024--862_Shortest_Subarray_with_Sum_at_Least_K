#include <iostream>
#include <vector>
#include <queue>
#include <limits>
using namespace std;

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

int main() {
    vector<int> nums = {2,-1,2};
    int k = 3;
    Solution sol;
    cout << sol.shortestSubarray(nums, k) << endl;
}