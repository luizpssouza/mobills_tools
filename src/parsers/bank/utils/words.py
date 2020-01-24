from dynaconf import settings

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


def is_ignored(line: str) -> bool:
    for contains_with in settings.IGNORE_LINES_CONTAINS_IN_FILE:
        if contains_with in line.lower():
            return True

    return False


def remove_lines_contains(lines):
    for line in lines:
        if not is_ignored(line):
            yield line
