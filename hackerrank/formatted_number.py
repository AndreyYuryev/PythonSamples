def print_formatted(number):
    # your code goes here
    length = len(format(number, 'b')) + 1
    for item in range(1, number + 1):
        line = list()
        sep = length - len(format(item, 'd')) - 1
        line.append(sep * ' ')
        line.append(format(item, 'd'))
        sep = length - len(format(item, 'o'))
        line.append(sep * ' ')
        line.append(format(item, 'o').upper())
        sep = length - len(format(item, 'x'))
        line.append(sep * ' ')
        line.append(format(item, 'x').upper())
        sep = length - len(format(item, 'b'))
        line.append(sep * ' ')
        line.append(format(item, 'b'))
        out = ''.join(line)
        print(out)


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)