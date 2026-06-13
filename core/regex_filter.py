import re


def filter_lines( lines, pattern):
    if not pattern:
        return lines
    
    try:
        regex = re.compile(pattern,re.IGNORECASE)

    except re.error as e:
        raise ValueError(f"invalid regex:{e}")
    

    return [line for line in lines if regex.search(line)]