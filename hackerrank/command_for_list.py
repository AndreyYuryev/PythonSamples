if __name__ == '__main__':
    N = int(input())
    mylist = []
    for itm in range(1, N + 1):
        line = input().split(' ')
        command = str(line[0])
        if command == 'insert':
            mylist.insert(int(line[1]), int(line[2]))
        elif command == 'print':
            print(mylist)
        elif command == 'remove':
            mylist.remove(int(line[1]))
        elif command == 'append':
            mylist.append(int(line[1]))
        elif command == 'sort':
            mylist.sort()
        elif command == 'pop':
            mylist.pop()
        elif command == 'reverse':
            mylist.reverse()
