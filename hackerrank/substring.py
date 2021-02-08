def count_substring(string, sub_string):
    index = 0
    counter = 0
    while index >= 0:
        index = string.find(sub_string, index)
        if index != -1:
            counter += 1
            index += 1
    return counter


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)