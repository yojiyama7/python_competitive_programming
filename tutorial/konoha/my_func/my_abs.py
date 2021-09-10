def my_abs(x):
    if x < 0:
        return -x
    return x

if __name__ == "__main__":
    QUERY = [-float('inf'), -10**100, -1000, -2, -1, 0, 1, 2, 1000, 1000, 10**100, float('inf'), 123456789]
    QUERY += [-100000000.23432, -3.2, -0.00001, 0.00, 0.0001, 0.1, 0.23421321, 2321312.23131]

    correct = 0
    for q in QUERY:
        if my_abs(q) == abs(q):
            correct += 1
            continue
        print(q, my_abs(q), abs(q))

    print(f"{correct}/{len(QUERY)}")
