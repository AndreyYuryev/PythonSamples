import simplenote

user = 'yuryev@yandex.ru'
password = 'Simplenote2019'
sn = simplenote.Simplenote(user, password)

notes = sn.get_note_list()
for note in notes[0]:
    print(note['tags'])
    print(note['content'])