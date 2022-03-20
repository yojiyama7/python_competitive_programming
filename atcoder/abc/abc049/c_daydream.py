s = input()

while s != "":
	is_match = False
	for word in ("dream", "dreamer", "erase", "eraser"):
		if s[-len(word):] == word:
			s = s[:-len(word)]
			is_match = True
	if is_match == False:
		print("NO")
		exit()
print("YES")

################################

# s = input()

# while "" != s:
#     result = False
#     for word in ("dream", "dreamer", "erase", "eraser"):
#         if s[-len(word):] == word:
#             s = s[:-len(word)]
#             result = True
#             break
#     if result == False:
#         break
# print("YES" if result else "NO")