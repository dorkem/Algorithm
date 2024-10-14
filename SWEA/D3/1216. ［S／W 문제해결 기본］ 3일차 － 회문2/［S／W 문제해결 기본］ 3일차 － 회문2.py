def compar(arr, leng):
    for lst in arr:
        for i in range(N-leng+1):
            for j in range(leng//2):
                if lst[i+j] != lst[i+leng-1-j]:
                    break
                else:
                    return True
    return False


T = 1
for tc in range(T):
    n = int(input())
    N = 100
    arr1 = [list(input()) for _ in range(N)]
    arr2 = list(map(list,zip(*arr1)))

    for leng in range(N,1,-1):
        if compar(arr1, leng) or compar(arr2,leng):
            break
    print(f"#{tc} {leng}")