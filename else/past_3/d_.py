N = int(input())
S = [input() for _ in range(5)]

pt = """.###..#..###.###.#.#.###.###.###.###.###.
.#.#.##....#...#.#.#.#...#.....#.#.#.#.#.
.#.#..#..###.###.###.###.###...#.###.###.
.#.#..#..#.....#...#...#.#.#...#.#.#...#.
.###.###.###.###...#.###.###...#.###.###."""
pattern_texts = pt.split()


patterns = []
for i in range(10):
    x = 1+i*4
    # print(x, x+3)
    patterns.append([pattern_texts[j][x:x+3] for j in range(5)])

t = ""
for i in range(N):
    x = 1+i*4
    t += str(patterns.index([S[j][x:x+3] for j in range(5)]))

print(t)