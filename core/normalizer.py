import re

def normalize(text):
    text = text.replace("\u00A0", " ")  # Replace non-breaking spaces with regular spaces

    lines = []

    for line in text.splitlines():
        line = re.sub(r"\s+", " ", line).strip()  # Replace multiple spaces with a single space and trim
        if line:
            lines.append(line)

    return lines