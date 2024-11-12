testcase = int(input())
for tc in range(1,testcase+1):
   s = list(input())
   m = ['a','e','i','o','u']
   stri = ""
   for i in s:
      if i not in m:
         stri += i
   print(f"#{tc} {stri}")