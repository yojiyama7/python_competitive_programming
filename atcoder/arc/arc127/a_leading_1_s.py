N_str = input()

N = int(N_str)
N_len = len(N_str)
ans = 0
# 桁数i
for i in range(1, N_len+1):
    # 1の個数j
    for j in range(1, i+1):
        x_l = int('1'*j + '0'*(i-j))
        x_r = int('1'*j + ('1'+'0'*i)[:i-j])
        y_l = int('1'*j + ('2'+'0'*i)[:i-j])
        y_r = int('1'*(j-1) + '2' + '0'*(i-j))
        # print(i, j, (x_l, x_r), (y_l, y_r))
        x_score = max(0, min(x_r, N+1) - x_l)
        y_score = max(0, min(y_r, N+1) - y_l)
        # print([x_score, y_score])
        ans += x_score*j
        ans += y_score*j

print(ans)
