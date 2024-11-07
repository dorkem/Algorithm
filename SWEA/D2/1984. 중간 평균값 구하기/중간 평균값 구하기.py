tc = int(input())
for i in range(1,tc+1):
    arr = list(map(int,input().split()))
    arr.sort()
    average = round(sum(arr[1:len(arr)-1]) / len(arr[1:len(arr)-1]))
    print(f"#{i} {average}")