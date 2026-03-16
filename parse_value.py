variables = {}

# -------------------------
# 値解析
# -------------------------

def parse_value(text):

    text = text.strip()

    # string
    if text.startswith('"') and text.endswith('"'):
        return text[1:-1]

    # list
    if text.startswith("[") and text.endswith("]"):
        items = text[1:-1].split()
        return [int(x) for x in items]

    # variable
    if text in variables:
        return variables[text]

    # number
    try:
        return int(text)
    except:
        return text
