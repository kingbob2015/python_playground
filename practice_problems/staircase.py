def numWaysDP(n, X):
    if n==0:
        return 1
    nums = [0] * (n+1)
    nums[0] = 1
    for i in range(1, n+1):
        total = 0
        for j in X:
            if i-j >= 0:
                total += nums[i-j]
        nums[i] = total
    return nums[n]

def numWaysRec(n, X):
    if n==0:
        return 1
    total = 0
    for i in X:
        if n-i >=0:
            total+=numWaysRec(n-i, X)
    return total

if __name__ == '__main__':
    n = 10
    X = {1, 3, 5}

    print(f"DP: {numWaysDP(n, X)}")
    print(f"Rec: {numWaysRec(n, X)}")