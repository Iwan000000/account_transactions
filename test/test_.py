import pytest
import json
from utils.arrs import sorted_json, mask_account_number


def test_sorted_json_returns_list():
    result = sorted_json()
    assert isinstance(result, list)

def test_sorted_json_returns_sorted_operations():
    with open('operations.json', encoding="utf-8",mode='r') as file:
        expected_data = json.load(file)

    expected_operations = [operation for operation in expected_data if 'date' in operation and 'from' in operation and operation.get('state') != 'CANCELED']

    expected_sorted_operations = sorted(expected_operations, key=lambda x: x['date'], reverse=True)

    result = sorted_json()

    assert result == expected_sorted_operations


def test_sorted_json():
    # Create a sample operations.json file with test data
    test_data = [
        {"date": "2022-07-15", "from": "Account A", "state": "SUCCESS"},
        {"date": "2022-07-14", "from": "Account B", "state": "SUCCESS"},
        {"date": "2022-07-16", "from": "Account C", "state": "CANCELED"}
    ]
    with open('operations.json', encoding="utf-8", mode='w') as file:
        json.dump(test_data, file)

    expected_result = [
        {"date": "2022-07-15", "from": "Account A", "state": "SUCCESS"},
        {"date": "2022-07-14", "from": "Account B", "state": "SUCCESS"}
    ]

    assert sorted_json() == expected_result

def test_mask_account_number_maestro():
    account_number = 'Maestro 1234567812345678'
    assert mask_account_number(account_number) == 'Maestro  1234 56** **** 5678'

def test_mask_account_number_visa_classic():
    account_number = 'Visa Classic 12345678901234567890'
    assert mask_account_number(account_number) == 'Visa Classic  1234 56** **** 567890'

def test_mask_account_number_visa_platinum():
    account_number = 'Visa Platinum 12345678901234567890'
    assert mask_account_number(account_number) == 'Visa Platinum  1234 56** **** 67890'

def test_mask_account_number_mastercard():
    account_number = 'MasterCard 12345678123456'
    assert mask_account_number(account_number) == 'MasterCard  1234 56** **** 3456'

def test_mask_account_number_visa_gold():
    account_number = 'Visa Gold 12345678901234'
    assert mask_account_number(account_number) == 'Visa Gold  1234 56** **** 1234'

def test_mask_account_number_visa_gold():
    account_number = 'Счет 12345678901234'
    assert mask_account_number(account_number) == '**** **** **** **** 1234'