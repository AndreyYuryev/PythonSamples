import json
import csv



cols = ['Id', 'Type', 'Name', 'Description', 'Priority', 'Status', 'Date', 'Deadline']
# csv_dict = dict.fromkeys(cols)
csv_list = list()

def parse_item(item_value, cols=cols, dict=csv_list, type='task'):
    for itm in item_value:
        if itm['_removed'] == 0:
            if type == 'task':
                upd_value = ['', type, itm['title'], itm['note'], itm['priority'], '', '', '']
            elif type == 'section':
                upd_value = ['', type, itm['title'], '', '', '', '', '']
            elif type == 'project':
                upd_value = ['', type, itm['title'], itm['note'], '', '', '', '']
            upd_dict = {k: v for k, v in zip(cols, upd_value)}
            csv_list.append(upd_dict)
        # for name_key, task_value in itm.items():
        #     if name_key == '_removed' and task_value == 1:
        #         break
        #     else:
        #         print(name_key, task_value)



with open( 'Database_20210611_104136.json', 'r', encoding='utf-8') as in_file:
    json_data = json.load(in_file)

js_data = json_data
for item in js_data.values():
    for key in item:
        if key == 'tasks':
            parse_item(item_value=item[key], cols=cols, dict=csv_list, type='task')
        elif key == 'taskGroups':
            parse_item(item_value=item[key], cols=cols, dict=csv_list, type='section')
        elif key == 'projects':
            # csv_dict.update(parse_project(task.items()))
            parse_item(item_value=item[key], cols=cols, dict=csv_list, type='project')
        else:
            pass



with open('database.csv', 'w', encoding='utf-8') as f:
    wr = csv.DictWriter(f, fieldnames=cols)
    wr.writeheader()
    for itm in csv_list:
        wr.writerow(itm)

