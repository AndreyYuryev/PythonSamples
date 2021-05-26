import pandas as pd

# card = pd.read_csv('C:/Out_file/card_8441.csv',
#                    delimiter=';',
#                    names=['Тип карты', 'Номер карты', 'Дата совершения операции',
#                           'Дата обработки операции', 'Код авторизации', 'Тип операции',
#                           'Город совершения операции', 'Страна совершения операции',
#                           'Описание', 'Валюта операции', 'Сумма в валюте операции', 'Сумма в валюте счета'])
# card = pd.read_csv('C:/Out_file/card_8441.csv', delimiter=';')
def read_xls():
    sales = pd.read_excel('C:/Out_file/pythonexcel.xlsx', sheet_name = 'sales')
    states = pd.read_excel('C:/Out_file/pythonexcel.xlsx', sheet_name = 'states')
    print(sales.head(6))
    sales['MoreThan500'] = ['Yes' if x > 500 else 'No' for x in sales['Sales']]
    print(sales.head(6))
    sales = pd.merge(sales, states, how='left', on='City')
    print(sales.head(6))
    new = sales.pivot_table(index='City', values='Sales', aggfunc='sum')
    print(new.head(6))
    #print(sales.tail())
    #for col in sales.columns:
    #    series = sales[col]
    #    print(series)

def read_card():
    # card = pd.read_csv('C:/Out_file/card_8441.csv', delimiter=';')
    card = pd.read_csv('C:/Out_file/card_8441.csv',
                       delimiter=';',
                       names=['Тип карты', 'Номер карты', 'Дата совершения операции',
                              'Дата обработки операции', 'Код авторизации', 'Тип операции',
                              'Город совершения операции', 'Страна совершения операции',
                              'Описание', 'Валюта операции', 'Сумма в валюте операции', 'Сумма в валюте счета'])
    # for col in card.columns:
    #     print(col)
    summa = 0.
    for lin in range(1,10):
        print('---', lin, '---')
        #for col in card.columns:
            #print(col, card[col][lin])
        print(card['Дата совершения операции'][lin], card['Сумма в валюте операции'][lin])
        summa += float(card['Сумма в валюте операции'][lin])
#         print('--')
    print('Итого:', summa)
# head = card.head()
# for itm in card:
#     print(itm.)
# print(card.columns)
# print(head)


if __name__ == '__main__':
    read_xls()
