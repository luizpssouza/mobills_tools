from .default import format_line
from .category import find as find_category
from .words import replace as replace_word


def process(lines: [str], bank_name: str):
    for line in lines:
        line = format_line(line)
        line += f',{bank_name}'
        line = find_category(line)
        line = replace_word(line)
        print(line)

    pass
