#include <iostream>
#include <vector>
#include <limits>
using namespace std;

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

int main() {
    vector<int> nums = {2,-1,2};
    int k = 3;
    Solution sol;
    cout << sol.shortestSubarray(nums, k) << endl;
}