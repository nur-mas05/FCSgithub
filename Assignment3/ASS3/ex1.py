def binary(arr, min, high, target):
    if min > high:
        return -1  # Target not found

    mid = (min + high) // 2

    if arr[mid] == target:
        return mid  # Target found
    elif arr[mid] < target:
        return binary(arr, mid + 1, high, target)  # Search in the right half
    else:
        return binary(arr, min, mid - 1, target)  # Search in the left half

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 5
result = binary(arr, 0, len(arr) - 1, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")
