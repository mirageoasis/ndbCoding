num_to_char = {
    3000 : "MMM",
    2000 : "MM",
    1000 : "M",
    
    900 : "CM",
    800 : "DCCC",
    700 : "DCC",
    600 : "DC",
    500 : "D",
    400 : "CD",
    300 : "CCC",
    200 : "CC",
    100 : "C",
    
    90 : "XC",
    80 : "LXXX",
    70 : "LXX",
    60 : "LX",
    50 : "L",
    40 : "XL",
    30 : "XXX",
    20 : "XX",
    10 : "X",
    
    9 : "IX",
    8 : "VIII",
    7 : "VII",
    6 : "VI",
    5 : "V",
    4 : "IV",
    3 : "III",
    2 : "II",
    1 : "I",
    
    0 : "",   
}

char_to_num = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}

a = input()
b = input()


def string_to_num(string):
    ret = 0

    if len(string) == 1:
        return char_to_num[string[0]]

    buffer=char_to_num[string[0]]
    for idx in range(1, len(string)):
        if char_to_num[string[idx]] > char_to_num[string[idx-1]]:
            buffer = char_to_num[string[idx]] - buffer
            ret+=buffer
            buffer=0
        else:
            ret+=buffer
            buffer=char_to_num[string[idx]]
    ret+=buffer
    return ret

ans = string_to_num(a) + string_to_num(b)
print(ans)

string = ""
n = 1000
while n > 0:
    real = ans // n * n
    string += num_to_char[real]
    ans -= real
    n //=10


print(string)