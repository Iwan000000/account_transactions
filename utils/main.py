from utils.arrs import mask_account_number, sorted_json

sorted = sorted_json()

def main_(sorted):
    """Основная функция"""

    for operation in sorted[:5]:
        date = operation['date'].split('T')[0]
        description = operation['description']
        from_account = operation['from']
        to_account = operation['to']
        amount = operation['operationAmount']['amount']
        currency = operation['operationAmount']['currency']['name']
        masked_from_account = mask_account_number(from_account)
        masked_to_account = mask_account_number(to_account)

        print(f"{date} {description}\n{masked_from_account} -> {masked_to_account}\n{amount} {currency}\n")

if __name__ == "__main__":
    main_(sorted)