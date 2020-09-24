m_list = list(map(int, input().split()))
for i in range(len(m_list)):
    if m_list[i] % 2 == 0:
        print(m_list[i], end=" ")
