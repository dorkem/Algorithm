def val(arr):
   if len(arr) != len(set(arr)):
      return 0
   else:
      return 1

t = int(input())
for tc in range(1, t+1):
   puzzle = [list(map(int,input().split())) for _ in range(9)]
   bol = True
   for i in range(9):
      if val(puzzle[i]) == 0:
         bol = False
         break
      arr = []
      for j in range(9):
         arr.append(puzzle[j][i])
      if val(arr) == 0:
         bol = False
         break
   
   for i in range(0,9,3):
      for j in range(0,9,3):
         arr = []
         for x in range(i,i+3):
            for y in range(j, j+3):
               arr.append(puzzle[x][y])

         if val(arr) == 0:
            bol = False
            break
   
   if bol == True:
      print(f"#{tc} 1")
   else:
      print(f"#{tc} 0")