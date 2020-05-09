s = input()
q = int(input())
query = [input().split() for _ in range(q)]

add_texts = ["", ""]
head = 0
for q_i in query:
    if q_i[0] == "1":
        head = ~head
    else:
        f, c = q_i[1:]
        if f == "1":
            add_texts[head] += c
        else:
            add_texts[~head] += c

text = add_texts[0][::-1] + s + add_texts[1]
print(text[::[1, -1][head]])