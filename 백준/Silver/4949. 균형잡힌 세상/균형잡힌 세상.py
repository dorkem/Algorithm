a = ['(', ')', '[', ']']
while True:
    b = input()
    stack = []
    if b == '.':
        break
    for char in b:
        if char not in a:
            continue
        if char in '([':
            stack.append(char)
        elif char == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(')')
                break
        elif char == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(']')
                break
    if len(stack) == 0:
      print('yes')
    else:
      print('no')
