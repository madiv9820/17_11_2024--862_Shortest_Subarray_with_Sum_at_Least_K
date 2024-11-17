# [862. Shortest Subarray with Sum at Least K](https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k)

__Type:__ Hard <br>
__Topics:__ Array, Binary Search, Queue, Sliding Window, Heap (Priority Queue), Prefix Sum, Monotonic Queue <br>
__Companies:__ Google, Meta, Goldman Sachs, Amazon, Microsoft
<hr>

Given an integer array `nums` and an integer `k`, return _the length of the shortest non-empty __subarray__ of_ `nums` _with a sum of at least_ `k`. If there is no such __subarray__, return `-1`.

A __subarray__ is a __contiguous__ part of an array.
<hr>

### Examples
- __Example 1:__ <br>
__Input:__ nums = [1], k = 1 <br>
__Output:__ 1

- __Example 2:__ <br>
__Input:__ nums = [1,2], k = 4 <br>
__Output:__ -1

- __Example 3:__ <br>
__Input:__ nums = [2,-1,2], k = 3 <br>
__Output:__ 3
<hr>

### Constraints:
- <code>1 <= nums.length <= 10<sup>5</sup></code>
- <code>-10<sup>5</sup> <= nums[i] <= 10<sup>5</sup></code>
- <code>1 <= k <= 10<sup>9</sup></code>