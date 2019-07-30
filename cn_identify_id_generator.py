import time
import datetime
import random
from cn_areacode_201807 import cncode

def get_birth_code():
    y = 1950 + random.randint(0,68)
    m = random.randint(1,12)
    d = 0;
    if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
        d = random.randint(1,31)
    elif m == 4 or m == 6 or m == 9 or m == 11:
        d = random.randint(1,30)
    elif m == 2:
        if y%400 == 0:
            d = random.randint(1,29)
        elif y%100 == 0:
            d = random.randint(1,28)
        elif y%4 == 0:
            d = random.randint(1,29)
        else:
            d = random.randint(1,28)

    code = str(y)
    if m < 10:
        code += "0"
    code += str(m)

    if d < 10:
        code += "0"
    code += str(d)
    return code

def get_validatation_code(in_code):
    if len(in_code) < 17:
        return "-1"
    validator = [7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
    sum = 0;
    try:
        for i in range(0,17):
            bit = int(in_code[i])
            sum += bit * validator[i]
    except Exception as e:
        print(e)
        return ""

    sum %= 11
    code = ['1','0','X','9','8','7','6','5','4','3','2']
    return code[sum]

def generate_identify_id():
    random_int = random.randint(0,3217)
    birth = get_birth_code()
    serialno = random.randint(1,999)
    identify_id = cncode[random_int]
    identify_id += birth
    if serialno < 10:
        identify_id += "00"
    elif serialno < 100:
        identify_id += "0"
    identify_id += str(serialno)
    validate_code = get_validatation_code(identify_id)
    if not validate_code:
        return ""

    identify_id += validate_code
    return identify_id


if __name__ == "__main__":
    print(generate_identify_id())
