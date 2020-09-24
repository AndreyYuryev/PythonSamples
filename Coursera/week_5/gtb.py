m_list = list(map(int, input().split()))
bef_val = m_list[0]
for i in range(1, len(m_list)):
    if m_list[i] > bef_val:
        print(m_list[i], end=" ")
    bef_val = m_list[i]
