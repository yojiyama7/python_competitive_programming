A, B = map(int, input().split(" "))

T = abs(A-B)

print(T//10 + [0, 1, 2, 3, 2, 1, 2, 3, 3, 2][T%10])

################################
#-------------------------------
################################

# T=abs(eval(input().replace(" ","-")));print(T//10+780004>>T%10*2&3)

# A,B=map(int,input().split());T=A-B
