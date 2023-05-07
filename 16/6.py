# lcs 

A = input()
B = input()

li = [[0 for i in range(len(B) + 1)] for j in range(len(A) + 1)]

for i in range(0, len(B) + 1):
    li[0][i] = i

for i in range(0, len(A) + 1):
    li[i][0] = i

for i in range(1, len(A) + 1):
    for j in range(1, len(B) + 1):
        if A[i - 1] == B[j - 1]:
            li[i][j] = li[i - 1][j - 1]
        else:
            li[i][j] = min(li[i][j-1], li[i-1][j], li[i-1][j-1]) + 1

# for i in li:
#    print(i)

print(li[len(A)][len(B)])