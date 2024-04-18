def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        # Check if target is present at mid
        if arr[mid] == target:
            return mid

        # If target is greater, ignore left half
        elif arr[mid] < target:
            left = mid + 1

        # If target is smaller, ignore right half
        else:
            right = mid - 1

    # If the element is not present in the array
    return -1

# Test the binary search function
def main():
    print("Binary Search Program") 
    arr = [2, 3, 4, 10, 40]
    target = int(input("Enter the number to search for: "))
    result = binary_search(arr, target)
    if result != -1:
        print("Element", target, "is present at index", result)
    else:
        print("Element", target, "is not present in array")

if __name__ == "__main__":
    main()