

reader={
    'I': 1,
    'IV': 4,
    'V': 5,
    'IX': 9,
    'X': 10,
    'XL': 40,
    'L': 50,
    'XC': 90,
    'C': 100,
    'CD': 400,
    'D': 500,
    'CM': 900,
    'M': 1000,
}


def read_number(string):
    
    # 왼쪽보다 커야함
    num=0
    now_string=string[0]
    for i in range(1, len(string)):
        if now_string+string[i] not in reader:
            num+=reader[now_string]
            now_string=string[i]
        else:
            now_string+=string[i]

    num+=reader[now_string]
    return num

number_dict ={
    0: '',
    
    1: 'I',
    2: 'II',
    3: 'III',
    4: 'IV',
    5: 'V',
    6: 'VI',
    7: 'VII',
    8: 'VIII',
    9: 'IX',

    10: 'X',
    20: 'XX',
    30: 'XXX',
    40: 'XL',
    50: 'L',
    60: 'LX',
    70: 'LXX',
    80: 'LXXX',
    90: 'XC',

    100: 'C',
    200: 'CC',
    300: 'CCC',
    400: 'CD',
    500: 'D',
    600: 'DC',
    700: 'DCC',
    800: 'DCCC',
    900: 'CM',

    1000: 'M',
    2000: 'MM',
    3000: 'MMM',
}


def to_string(number):
    thousand=number_dict[number//1000*1000]
    hundred=number_dict[number%1000//100*100]
    ten=number_dict[number%100//10*10]
    one=number_dict[number%10]

    return thousand+hundred+ten+one

a=input()
b=input()

num= read_number(a) + read_number(b)

#print(read_number(a))
#print(read_number(b))
print(num)
print(to_string(num))
