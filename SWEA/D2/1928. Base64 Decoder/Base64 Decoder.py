table = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 
    'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 
    'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 
    'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '/'
]

t = int(input())
for tc in range(1, t+1):
    n = list(input())
    m = ""
    for i in range(0, len(n), 4):
        num = n[i:i+4]
        arr = []
        st = "" 
        for j in num:
            arr = table.index(j)
            st += format(int(arr),'06b')
        
        for j in range(0, len(st), 8):
            byte = st[j:j+8]
            m += chr(int(byte, 2))
            
    print(f"#{tc} {m}")