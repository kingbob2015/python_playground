def binary_search(arr, target):
    low,high = 0, len(arr)-1
    while(low<=high):
        mid=(high+low)//2
        if arr[mid]==target:
            return mid
        elif arr[mid] < target:
            low = mid+1
        else:
            high = mid-1
    return -1

if __name__ == '__main__':
    test = [1,2,3,4,10,20,500]
    print(binary_search(test, 20))