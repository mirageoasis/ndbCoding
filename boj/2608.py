a = input()
b = input()

small = {
    "IV" : 4,
    "IX" : 9,
    "XL" : 40,
    "XC" : 90,
    "CD" : 400,
    "CM" : 900,
}

normal = {
    "I" : 1,
    "V" : 5,
    "X" : 10,
    "L" : 50,
    "C" : 100,
    "D" : 500,
    "M" : 1000,
}

def to_num(string : str):
    ret = 0 
    for i in small:
        if string.find(i) != -1:
            string = string.replace(i, '')
            ret += small[i]
    for i in string:
        ret += normal[i]

    return ret

def convert_to_string(total_ans):
    ret = ''
    thousand = total_ans // 1000
    hund = total_ans % 1000 // 100
    ten = total_ans % 100 // 10
    one = total_ans % 10

    ret += 'M' * thousand

    if hund >= 5:
        if hund == 9:
            ret += 'CM'
        else:
            ret += 'D'
            ret += 'C' * (hund - 5)
    else:
        if hund == 4:
            ret += 'CD'
        else:
            ret += 'C' * hund

    if ten >= 5:
        if ten == 9:
            ret += 'XC'
        else:
            ret += 'L'
            ret += 'X' * (ten - 5)
    else:
        if ten == 4:
            ret += 'XL'
        else:
            ret += 'X' * ten

    if one >= 5:
        if one == 9:
            ret += 'IX'
        else:
            ret += 'V'
            ret += 'I' * (one - 5)
    else:
        if one == 4:
            ret += 'IV'
        else:
            ret += 'I' * one

    return ret


ans_a = to_num(a)
ans_b = to_num(b)

total_ans = ans_a + ans_b

print(total_ans)
print(convert_to_string(total_ans))