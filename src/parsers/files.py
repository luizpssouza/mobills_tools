import csv
import glob
import os
import time
import sys


from dynaconf import settings


import parsers.bank as parser_bank


def list_files():
    files_path = glob.glob(
        f"{settings.PATH_CONTAINS_BANK_STATEMENT_FILES}/*.txt"
    )
    for file_path in files_path:
        read_file(file_path)


def read_file(file: str):
    file_name_as_bank, extension = os.path.splitext(os.path.basename(file))
    bank = parser_bank.get_bank(file_name_as_bank)

    print("#################")
    print(bank.__name__)
    print("#################")

    with open(file, "r") as file:
        lines_of_file = file.readlines()
        data = bank.process(lines_of_file, file_name_as_bank)
        save_csv('result', data)


def save_csv(result_file_name: str, data: [tuple]):
    file_name = (f'{settings.PATH_CONTAINS_BANK_STATEMENT_FILES}'
                 f'/{result_file_name}_{time.strftime("%Y-%m-%d %H:%M:%S")}.csv')

    with open(
        file_name,
        'w',
        encoding='ISO-8859-15'
    ) as out:
        csv_out = csv.writer(out)
        csv_out.writerow(settings.MOBILLS_CSV_HEADER)
        for row in data:
            csv_out.writerow(row)
