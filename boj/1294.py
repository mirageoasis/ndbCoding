import sys

input = sys.stdin.readline
n = int(input())
strings = []
lens = 0
for i in range(n):
    tmp = input().strip()
    lens += len(tmp)
    strings.append(tmp)

idxs = [0 for i in range(n)]

total_cnt = 0
ans = ""
while total_cnt < lens:

    min_letter = 'ZZ'
    target_string_idx = -1
    #print()
    #print(ans)
    #print(idxs)
    for challenge_idx in range(len(strings)):
        # 이미 다 소진했으면 ㅂㅂ
        now_idx = idxs[challenge_idx]
        now_string = strings[challenge_idx]
        #print("NO TO CMP", min_letter, target_string_idx, challenge_idx)
        if now_idx == len(now_string):
            continue
        now_letter = now_string[now_idx]

        if min_letter > now_letter:
            min_letter = now_letter
            target_string_idx = challenge_idx
            continue

        if min_letter == now_letter:
            candidate_string = strings[target_string_idx]
            candidate_idx = idxs[target_string_idx]
            compare_idx = min(len(now_string) - now_idx, len(candidate_string) - candidate_idx)

            for j in range(compare_idx):
                if now_string[now_idx + j] == candidate_string[candidate_idx + j]:
                    continue

                if now_string[now_idx + j] < candidate_string[candidate_idx + j]:
                    min_letter = now_letter
                    target_string_idx = challenge_idx
                break
            else:
                if len(candidate_string) - candidate_idx < len(now_string) - now_idx:
                    min_letter = now_letter
                    target_string_idx = challenge_idx

    #print(target_string_idx, idxs[target_string_idx], strings[target_string_idx])
    ans += strings[target_string_idx][idxs[target_string_idx]]
    idxs[target_string_idx] += 1

    total_cnt += 1

print(ans)