import re

def contains_infix_expression(query: str):
    query_without_brackets = re.sub(r'\(|\)', "", query)
    query_without_brackets = query_without_brackets.replace("  ", " ")
    return re.match(r'^\s*\d+( [+/\-*] \d+)*\s*$', query_without_brackets)

def contains_date(query: str):
    if re.match(r'\d{4}-\d{2}-\d{2}', query):
        return True
    
    match = re.match(r'\d{1, 2} (\w+) \d{4}', query) 
    if match is not None and match.groups()[0].lower() in ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']:
        return True

    return False
