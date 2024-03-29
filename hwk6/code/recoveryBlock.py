def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key
    return arr

def is_sorted(arr):
    return all(arr[i] <= arr[i+1] for i in range(len(arr)-1))

def sort_with_recovery(arr):
    print("Attempting primary variant (QuickSort)")
    sorted_arr = quicksort(arr)
    if is_sorted(sorted_arr):
        print("Primary variant succeeded.")
        return sorted_arr
    else:
        print("Primary variant failed. Attempting alternate variant (InsertionSort)")
        sorted_arr = insertion_sort(arr)
        if is_sorted(sorted_arr):
            print("Alternate variant succeeded.")
            return sorted_arr
        else:
            print("All variants failed.")
            raise Exception("Recovery failed.")

arr = [3, 2, 5, 1, 6, 4]
sorted_arr = sort_with_recovery(arr)
print("Sorted array:", sorted_arr)
