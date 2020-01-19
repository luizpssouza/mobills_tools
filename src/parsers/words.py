REPLACES = [
    ('Resgate - ', ''),
    ('Compra de Cartão - ', ''),
    ('Aplicação - ', ''),
]


def replace(line: str) -> str:
    for replace_word in REPLACES:
        line = line.replace(
            replace_word[0], replace_word[1])
    return line
