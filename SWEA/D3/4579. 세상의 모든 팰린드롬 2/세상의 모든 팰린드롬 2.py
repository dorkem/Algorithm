t = int(input())

for tc in range(1, t + 1) :
    data = input()
    reversed_data = data[::-1]
    result = 'Not exist'
    for i in range(len(data)) :
        if data[i] == reversed_data[i] :
            continue
        if data[i] == '*' or reversed_data[i] == '*' :
            result = 'Exist'
            break
        else :
            break
    else :
        result = 'Exist'

    print('#%d %s' % (tc, result))