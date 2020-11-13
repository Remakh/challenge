import re

def contains_date(query: str):
    if re.match(r'\d{4}-\d{2}-\d{2}', query):
        return True
    
    match = re.match(r'\d{1, 2} (\w+) \d{4}', query) 
    if match is not None and match.groups()[0].lower() in ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']:
        return True

    return False
