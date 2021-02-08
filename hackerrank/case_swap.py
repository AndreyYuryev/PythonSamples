def swap_case(s):
    case_string = []
    for itm in s:
        if itm.isupper():
            case_string.append(itm.lower())
        elif itm.islower():
            case_string.append(itm.upper())
        else:
            case_string.append(itm)
    return ''.join(case_string)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)