a = []
a.append(input())
a.append(input())
a.append(input())
inum = 0
num = 0
for i in range(len(a)):
    if ord(a[i][0]) < 65:
        inum = 3-i
        num = a[i]
        break
inum = int(num) + inum
if inum % 15 == 0:
    print("FizzBuzz")
elif inum % 3 == 0 and inum % 5 !=0:
    print("Fizz")
elif inum % 3 !=0 and inum % 5 == 0:
    print("Buzz")
else:
    print(inum)