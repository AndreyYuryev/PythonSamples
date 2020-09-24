st = input()
pos_split = st.find(" ")
new_st = st[pos_split + 1:] + " " + st[:pos_split]
print(new_st)
