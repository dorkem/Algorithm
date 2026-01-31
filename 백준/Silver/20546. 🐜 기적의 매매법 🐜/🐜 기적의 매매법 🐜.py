money = int(input())
price = list(map(int, input().split()))

j_money = money
j_stock = 0
s_money = money
s_stock = 0

up = 0
down = 0

for i in range(len(price)):
    if price[i] <= j_money:
        buy = j_money // price[i]
        j_stock += buy
        j_money -= buy * price[i]

    if i >= 1:
        if price[i-1] > price[i]:
            down += 1
            up = 0
        elif price[i-1] < price[i]:
            up += 1
            down = 0
        else:
            up = 0
            down = 0

        if down >= 3:
            buy = s_money // price[i]
            s_stock += buy
            s_money -= buy * price[i]

        elif up >= 3:
            s_money += s_stock * price[i]
            s_stock = 0

j_total = j_money + j_stock * price[-1]
s_total = s_money + s_stock * price[-1]

if j_total > s_total:
    print("BNP")
elif j_total < s_total:
    print("TIMING")
else:
    print("SAMESAME")
