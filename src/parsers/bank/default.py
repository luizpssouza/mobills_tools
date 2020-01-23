def separators_for_mobills(line: str):
    return (
        line
        .replace('  ', ' ', -1)
        .replace('\t\t', '\t', -1)
        .replace('\t', ',', -1)
        .replace('\n', '', -1)
    )


def remove_invalid_chars_for_mobills(line: str):
    return line.replace('R$', '', -1).replace('.', '', -1).replace(',', '.', -1)


def format_line(line: str):
    line = remove_invalid_chars_for_mobills(line)
    line = separators_for_mobills(line)
    return line
