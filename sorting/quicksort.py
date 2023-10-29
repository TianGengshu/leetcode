def partition(arr):
    pivot,low,high = len(arr)-1,0,len(arr)-2
    while low < high:
        if arr[low]> arr[pivot]:
            arr[low],arr[high] = arr[high],arr[low]
            high -=1
        low+=1

    # swap pivot and low
    arr[low],arr[pivot] = arr[pivot],arr[low]


def quick_sort(array):
    if not array:
        return
    partition(arr[])


if __name__ == "__main__":
    arr = [1,2,3,54,3]

    # print(quick_sort(arr))
    partition(arr)
    print(arr)