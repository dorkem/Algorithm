num = int(input())

for i in range(1,num+1):
    cnt = 0
    string = str(i)
    if "3" in string or "6" in string or "9" in string:
        for j in string:
            if j == "3" or j == "6" or j == "9":
                cnt += 1
        string = "-" * cnt
    print(string, end=" ")