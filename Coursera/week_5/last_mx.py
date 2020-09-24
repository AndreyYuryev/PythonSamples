m_list = list(map(int, input().split()))
max_ind = 0
max_val = m_list[0]
for i in range(1, len(m_list)):
    if m_list[i] >= max_val:
        max_val = m_list[i]
        max_ind = i
print(max_val, max_ind, sep=" ")
