from time import sleep

def to_mark(s):
    return s.replace("W", "#").replace("R", "=").replace("B", "-")

def solve_upblock(a, b):
    if a == b:
        return a
    s = set("WRB")
    s.remove(a)
    s.remove(b)
    return list(s)[0]

def generate_pyramid(l):
    p = [l]
    while len(l) > 1:
        next_l = [solve_upblock(l[j], l[j+1]) for j in range(len(l)-1)]
        l = next_l
        p.append("".join(l))
    return (p[::-1])

S = input()
N = len(S)
# print()
[print(" "*(N-i)+to_mark(line)) for i, line in enumerate(generate_pyramid(S))]
# print()

# for i, line in enumerate(generate_pyramid(S)[::-1]):
#     print('\r' + line, end=" "*i)
#     sleep(1)
