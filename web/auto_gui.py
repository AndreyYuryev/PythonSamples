from pywinauto.application import Application


app = Application(backend='uia').start("notepad.exe")
dlg = app.window(best_match='Безымянный')


dlg.print_control_identifiers(depth=3)
menu = dlg.Menu2
item = menu.MenuItem
item.print_control_identifiers()

item['click']

menu.select()
menu.MenuItem(best_match='Файл').click()
# menu_select("File").click()

#mi = dlg_spec.MenuItem('Файл')
#edit1 = dlg_spec['Файл'].wrapper_object()
#edit1.type_keys('test')
# Опишем окно, которое хотим найти в процессе Notepad.exe
# dlg_spec = app['Безымянный']
# ждем пока окно реально появится
# actionable_dlg = dlg_spec.wait('visible')

#dlg_spec.wrapper_object('Файл->Сохранить')
