from sys import argv
from csv import DictReader

def csv_dict_reader(file_obj):
    """
    Read a CSV file using csv.DictReader
    """
    reader = DictReader(file_obj.name, delimiter=";")
    for line in reader:
        print(line)
        #  print(line["first_name"]),
        #  print(line["last_name"])


if __name__ == "__main__":
    #  p_name = argv[0]
    #  p_first = argv[1]
    #  p_second = argv[2]
    with open("1.csv", "r", encoding='cp1251') as f_obj:
        # csv_dict_reader(f_obj)
        fieldname = ['field1', 'field2']
        dc = DictReader(f=f_obj, fieldnames=fieldname, delimiter=';')
        z = list(map(str, dc.reader))
        print(z)
        #for line in reader:
        #    print(line)