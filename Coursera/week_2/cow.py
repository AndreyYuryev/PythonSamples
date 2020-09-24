cows = input()
i_cows = int(cows)
if i_cows == 1 or ((i_cows - 1) % 10 == 0 and i_cows != 20 and i_cows > 20):
    print(cows + ' ' + 'korova')
elif 2 <= i_cows <= 4 or (i_cows > 20 and 2 <= i_cows % 10 <= 4):
    print(cows + ' ' + 'korovy')
elif i_cows == 0 or 5 <= i_cows <= 20:
    print(cows + ' ' + 'korov')
elif i_cows > 20 and (5 <= i_cows % 10 <= 9 or i_cows % 10 == 0):
    print(cows + ' ' + 'korov')
