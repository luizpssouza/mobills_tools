COST_TEXT_TO_CATEGORY = [
    ('google play', 'Internet'),
    ('compre bem', 'Mercado'),
    ('Uber', 'Uber'),
]


def find(line: str) -> str:
    for cost_text_category in COST_TEXT_TO_CATEGORY:
        cost = cost_text_category[0]
        if cost.lower() in line.lower():
            return line + ',' + cost_text_category[1]
    return line + ',Outros'
