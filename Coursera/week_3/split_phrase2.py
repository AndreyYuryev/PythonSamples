st = input()
space_count = st.count(" ")
counter = 0
pos = 0
length = len(st)
if space_count == 0:
    print(1)
else:
    while pos < length:
        counter += 1
        pos = st.find(" ", pos)
        if pos != -1:
            pos += 1
        else:
            pos = length
    print(counter)
