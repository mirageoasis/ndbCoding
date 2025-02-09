def find_kth_digit(n, k):
    # 1. 자리수별 숫자 개수 저장
    length = 0
    num = 1
    digit_count = []

    while num <= n:
        next_num = num * 10
        count = min(n - num + 1, next_num - num) * len(str(num))
        digit_count.append(count)
        length += count
        num = next_num

    # 전체 길이보다 k가 크면 -1
    if k > length:
        return -1

    # 2. k를 음수가 되기 전까지 빼면서 자리수 찾기
    num = 1
    digit_length = 1
    while k > digit_count[digit_length - 1]:
        k -= digit_count[digit_length - 1]
        num *= 10
        digit_length += 1

    # 3. k // (자리수) 와 k % (자리수) 구하기
    index = (k - 1) // digit_length
    digit_index = (k - 1) % digit_length

    # 4. 해당 자리수에서 (몫 + 1) 번째 수 구하기
    target_number = num + index

    # 5. target_number의 digit_index 번째 자리 숫자 출력
    return str(target_number)[digit_index]

# 입력 받기
n, k = map(int, input().split())
print(find_kth_digit(n, k))
