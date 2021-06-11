A = """puvxlhwva
fubxha
tbxvtralb
jnerjnerun
xvzvgnpuvgb
lhxban
xnaxrvjb
xvmhxhgnzr
xbabubfuvav
lnggrxvgn
fnffbxhqntn
lhxbab
fuvehfuvgbfvgr
chermragbjb
bartnvfuvgnv
ranwvqbevaxh
mbar
jb
whaovfuvgr
ubfuvvabqn
xbabartnvjb
xnanrgrxhereron
bgbanfuvxh
xbabubfuvjb
ngbavfhehgfhzbevqn
jnerjnerun
nenfbvtbgbjb
abmbznanv
znrzhxvan
urawvjb
xvgnvfuvgrveh
""".split()

def rot13(S):
    t = ""
    for c in S:
        x = ord(c)-ord('a')
        x += 13
        x %= 26
        t += chr(x + ord('a'))
    return (t)

# print(rot13("aiueo"))

print(*map(rot13, A), sep="\n")