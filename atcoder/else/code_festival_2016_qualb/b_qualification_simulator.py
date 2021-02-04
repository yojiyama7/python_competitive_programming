N, A, B = map(int, input().split())
S = input()

cnt = 0
abroad_cnt = 0
for s in S:
    if s == "a" and cnt < A + B:
        print("Yes")
        cnt += 1
    elif s == "b" and cnt < A + B and abroad_cnt < B:
        print("Yes")
        cnt += 1
        abroad_cnt += 1
    else:
        print("No")
