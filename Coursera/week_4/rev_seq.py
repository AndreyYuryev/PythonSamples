def rev_seq():
    a = int(input())
    if a != 0:
        rev_seq()
        print(a)
    else:
        print(a)

rev_seq()
