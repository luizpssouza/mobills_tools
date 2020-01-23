import parsers.bank.sofisa as sofisa_bank
import parsers.bank.santander as santander_bank


def get_bank(bank: str) -> sofisa_bank or santander_bank:
    if bank in 'sofisa':
        return sofisa_bank
    if bank in 'santander':
        return santander_bank
