m_list = list(map(int, input().split()))
posit_qty = 0
for i in range(len(m_list)):
    if m_list[i] > 0:
        posit_qty += 1
print(posit_qty)
