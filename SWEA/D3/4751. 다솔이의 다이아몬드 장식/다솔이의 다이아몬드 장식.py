t = int(input())
for tc in range(1,t+1):
    n = input()
    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""
    line5 = ""

    for i in range(len(n)):
        line1 += "..#."
        line2 += ".#.#"
        line3 += f"#.{n[i]}."
        line4 += ".#.#"
        line5 += "..#."

    print(line1+'.')
    print(line2+'.')
    print(f"{line3}#")
    print(line4+'.')
    print(line5+'.')