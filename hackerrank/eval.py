x, k = input().split(' ')
p = str(input())
p_out = list()
for itm in p:
    if itm == 'x':
        p_out.append(x)
    else:
        p_out.append(itm)
out_str = ''.join(p_out)
out = eval(out_str)

if out == int(k):
    print(True)
else:
    print(False)
