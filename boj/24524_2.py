s=input()
t=input()

letter_dict=dict()

chart=[0 for i in range(len(t))]

for idx, val in enumerate(t):
    letter_dict[val]=idx

for letter in s:
    # t에 있는 글자 중에서 자신보다 idx가 작은 글자들 빈도를 센다.
    #print(letter, letter_dict, letter_dict.get(letter))
    if letter not in letter_dict:
        continue
    #print(letter, t[0])
    if letter == t[0]:
        chart[0]+=1
    else:
        former_val=chart[letter_dict[letter]-1]

        chart[letter_dict[letter]] = min(chart[letter_dict[letter]]+1, former_val)
#print(chart)

print(chart[-1])