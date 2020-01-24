from .default import format_line
from .utils.category import find as find_category
from .utils.words import (
    replace as replace_word,
    remove_lines_contains as remove_lines_contains_word)


def process(lines: [str], bank_name: str) -> [tuple]:
    lines = remove_lines_contains_word(lines)

    data = []
    for line in lines:
        line = format_line(line)
        line += f',{bank_name}'
        line = find_category(line)
        line = replace_word(line)
        data.append(tuple(line.split(',')))
        print(line)

    return data
