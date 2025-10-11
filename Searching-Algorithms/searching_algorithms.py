"""
Title: Searching Algorithms in Python
Author: Tathagat Gaikwad
Contribution: Hacktoberfest 2025
Repository: https://github.com/A-K-0/HACKTOBERFEST_25_Python

Description:
This script contains multiple searching algorithms implemented in Python:
1. Linear Search
2. Binary Search (Iterative & Recursive)
3. Ternary Search
4. Jump Search
5. Exponential Search
"""

import math


# 1️⃣ Linear Search
def linear_search(arr, target):
    """Simple linear search."""
    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1


# 2️⃣ Binary Search (Iterative)
def binary_search_iterative(arr, target):
    """Binary search using an iterative approach (array must be sorted)."""
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


# 3️⃣ Binary Search (Recursive)
def binary_search_recursive(arr, target, left, right):
    """Binary search using recursion (array must be sorted)."""
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)


# 4️⃣ Ternary Search
def ternary_search(arr, target, left, right):
    """Ternary search divides the array into three parts."""
    if left > right:
        return -1
    mid1 = left + (right - left) // 3
    mid2 = right - (right - left) // 3

    if arr[mid1] == target:
        return mid1
    if arr[mid2] == target:
        return mid2

    if target < arr[mid1]:
        return ternary_search(arr, target, left, mid1 - 1)
    elif target > arr[mid2]:
        return ternary_search(arr, target, mid2 + 1, right)
    else:
        return ternary_search(arr, target, mid1 + 1, mid2 - 1)


# 5️⃣ Jump Search
def jump_search(arr, target):
    """Jump search for sorted arrays."""
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0

    while prev < n and arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1

    for i in range(prev, min(step, n)):
        if arr[i] == target:
            return i
    return -1


# 6️⃣ Exponential Search
def exponential_search(arr, target):
    """Exponential search for sorted arrays."""
    n = len(arr)
    if n == 0:
        return -1
    if arr[0] == target:
        return 0

    i = 1
    while i < n and arr[i] <= target:
        i *= 2

    return binary_search_recursive(arr, target, i // 2, min(i, n - 1))


# ✅ Example Execution
if __name__ == "__main__":
    arr = [1, 4, 7, 10, 14, 18, 21, 25, 29, 33, 37]
    target = 18

    print(f"Array: {arr}")
    print(f"Target: {target}\n")

    print("Linear Search Index:", linear_search(arr, target))
    print("Binary Search (Iterative) Index:", binary_search_iterative(arr, target))
    print("Binary Search (Recursive) Index:", binary_search_recursive(arr, target, 0, len(arr) - 1))
    print("Ternary Search Index:", ternary_search(arr, target, 0, len(arr) - 1))
    print("Jump Search Index:", jump_search(arr, target))
    print("Exponential Search Index:", exponential_search(arr, target))
