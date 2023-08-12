import csv
from http import HTTPStatus

def get_websites(csv_path: str) -> list[str]:
    """Loads websites from a csv file"""
    websites: list[str] = []
    try:
        with open(csv_path, 'r') as file:
            reader = csv.reader(file)
    except Exception as _:
        print(f"Cannot read {csv_path}")
    else:
        for row in reader:
            if row[0][:1] == "#":
                continue
            if 'https://' not in row[1]:
                websites.append(f'https://{row[1]}')
            else:
                websites.append(row[1])

    return websites


def get_status_description(status_code: int) -> str:
    """Uses the status code to return a readable description"""

    for value in HTTPStatus:
        if value == status_code:
            description: str = f'({value} {value.name}) {value.description}'
            return description

    return '(???) Unknown status code...'

if __name__ == '__main__':
