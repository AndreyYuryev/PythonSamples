n = int(input())
num_Sq = n
eqSq = 0
max_eqSq = 0
while n != 0:
    if n != 0 and n != num_Sq:
        num_Sq = n
        eqSq = 1
    elif n != 0 and n == num_Sq:
        eqSq += 1
        if max_eqSq < eqSq:
            max_eqSq = eqSq
    n = int(input())
else:
    print(max_eqSq)
