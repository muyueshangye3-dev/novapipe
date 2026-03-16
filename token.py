
# -----------------------------
# TOKEN
# -----------------------------

class Token:
    def __init__(self, t, v):
        self.type = t
        self.value = v




# -----------------------------
# LEXER
# -----------------------------

def tokenize(code):

    tokens = []

    for line in code.split("\n"):

        line = line.strip()

        if not line:
            continue

        parts = line.split()

        for p in parts:

            if p == "|":
                tokens.append(Token("PIPE", p))

            elif p == "<-":
                tokens.append(Token("ASSIGN", p))

            elif p == "{":
                tokens.append(Token("LBRACE", p))

            elif p == "}":
                tokens.append(Token("RBRACE", p))

            elif p.isdigit():
                tokens.append(Token("NUMBER", int(p)))

            else:
                tokens.append(Token("IDENT", p))

        tokens.append(Token("EOL", None))

    return tokens

