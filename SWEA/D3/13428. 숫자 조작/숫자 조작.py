from itertools import combinations

t = int(input())
for tc in range(1, t+1):

    n = list(input().strip())
    min_value = int(''.join(n))
    max_value = int(''.join(n))

    target = [i for i in range(len(n))]

    for i,j in combinations(target, 2):
        n[i], n[j] = n[j], n[i]
        if n[0] == '0':
            n[i], n[j] = n[j], n[i]
            continue

        compare = int(''.join(n))
        if compare < min_value:
            min_value = compare
        if max_value < compare:
            max_value = compare
        n[i], n[j] = n[j], n[i]

    print(f"#{tc} {min_value} {max_value}")