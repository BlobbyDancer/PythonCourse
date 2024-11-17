# TODO импортировать необходимые молули
import json
import csv

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, newline='', encoding='utf-8') as csvfile:
        # TODO считать содержимое csv файла
        reader = csv.DictReader(csvfile)
        data = [row for row in reader]

    with open(OUTPUT_FILENAME, 'w', encoding='utf-8') as jsonfile:
        # TODO Сериализовать в файл с отступами равными 4
        json.dump(data, jsonfile, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME, encoding='utf-8') as output_f:
        for line in output_f:
            print(line, end="")
