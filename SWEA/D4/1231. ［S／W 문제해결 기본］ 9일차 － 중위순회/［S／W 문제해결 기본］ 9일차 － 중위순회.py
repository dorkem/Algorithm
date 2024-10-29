class node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def in_order(node):
    if node is not None:
        in_order(node.left)
        print(node.value, end='')
        in_order(node.right)
T = 10
for t in range(1,T+1):
    tc = int(input())
    nodes = {}
    arr = [list(map(str, input().split())) for _ in range(tc)]
    for i in arr:
        index = int(i[0])
        value = i[1]
        if index not in nodes:
            nodes[index] = node(value)
        else:
            nodes[index].value = value
        
        if len(i) > 2:
            ln = int(i[2])
            if ln not in nodes:
                nodes[ln] = node(arr[ln - 1][1])  # 즉시 생성 및 설정
            nodes[index].left = nodes[ln]
        
        if len(i) > 3:
            rn = int(i[3])
            if rn not in nodes:
                nodes[rn] = node(arr[rn - 1][1])
            nodes[index].right = nodes[rn]
    print(f"#{t}", end=' ')
    in_order(nodes[1])
    print()