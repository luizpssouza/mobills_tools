from ast import literal_eval

from dynaconf import settings


def find(line: str) -> str:
    cost_text_to_category = literal_eval(settings.COST_TEXT_TO_CATEGORY)
    for cost_text_category in cost_text_to_category:
        cost = cost_text_category[0]
        if cost.lower() in line.lower():
            return line + ',' + cost_text_category[1]
    return line + ',Outros'
