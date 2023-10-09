import json


def sorted_json():
    """Функция открывает json файл и сортирует его """

    with open('operations.json', encoding="utf-8", mode='r') as file:
        datas = json.load(file)

    operations = [operation for operation in datas if 'date' in operation and datas if 'from' in operation and operation.get('state') != 'CANCELED']

    sorted_operations = sorted(operations, key=lambda x: x['date'], reverse=True)

    return sorted_operations


def mask_account_number(account_number):
    """Функция кодирует номера карт"""

    if account_number.startswith('Maestro'):
        masked_number = account_number[0:8] + ' ' + account_number[8:12] + ' ' + account_number[12:14] + '**' + ' **** ' + account_number[-4:]

    elif account_number.startswith('Visa Classic'):
        masked_number = account_number[0:12] + ' ' + account_number[12:17] + ' ' + account_number[17:19] + '**' + ' **** ' + account_number[-4:]

    elif account_number.startswith('Visa Platinum'):
        masked_number = account_number[0:13] + ' ' + account_number[13:18] + ' ' + account_number[18:20] + '**' + ' **** ' + account_number[-4:]

    elif account_number.startswith('MasterCard'):
        masked_number = account_number[0:10] + account_number[10:15] + ' ' + account_number[14:16] + '**' + ' **** ' + account_number[-4:]

    elif account_number.startswith('Visa Gold'):
        masked_number = account_number[0:9] + ' ' + account_number[9:14] + ' ' + account_number[14:16] + '**' + ' **** ' + account_number[-4:]

    elif account_number.startswith('Счет'):
        masked_number = '*' * 4 + ' ' + '*' * 4 + ' ' + '*' * 4 + ' ' + '*' * 4 + ' ' + account_number[-4:]

    else:
        masked_number = account_number

    return masked_number
