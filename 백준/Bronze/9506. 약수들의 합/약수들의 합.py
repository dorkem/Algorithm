while 1:
  a = int(input())
  if a == -1:
    break
  list = []
  for i in range(1,a):
    if a%i == 0:
      list.append(i)
  if sum(list) == a:
      print(a, " = ", " + ".join(str(i) for i in list), sep="")
  else:
      print(a, "is NOT perfect.")