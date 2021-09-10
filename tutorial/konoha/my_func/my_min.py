def my_min(a, *l):
    if not l:
        a, *l = a
    ans = a
    for li in l:
        if li < ans:
            ans = li
    return ans

if __name__ == "__main__":
    QUERY = [
        [1, 2, 3],
        [4, 3, 2, 1],
        [-10, 2, 3, 4],
        [10, 33, 2, 3],
        [4, 4],
        [-10, -10, -10, 199],
        ["abc", "def", "ghi"],
        ["abc", "abc"],
        [["a", "b", "c"], ["f"], ["d", "e"]],
        [[1]],
        [[-1]],
        [[0]],
        [[float("inf")]],
        [[-float("inf")]],
        [["gcd"]],
        [[-10, 2, 3, 4]],
        [[123, 9], [78, 456]],
        [list(range(10**6))],
    ]

    correct = 0
    for query in QUERY:
        if my_min(*query) == min(*query):
            correct += 1
            continue
        print(query, my_min(*query), min(*query))

    print(f"{correct}/{len(QUERY)}")
