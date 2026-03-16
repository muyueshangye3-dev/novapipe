from astnodes import Pipeline,Operation
from astnodes import Assignment,BlockDef

# -----------------------------
# PARSER
# -----------------------------

class Parser:

    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def peek(self):
        return self.tokens[self.pos]

    def advance(self):
        self.pos += 1

    def parse(self):

        tok = self.peek()

        if tok.type == "IDENT" and tok.value == "block":
            return self.parse_block()

        if tok.type == "IDENT" and self.tokens[self.pos+1].type == "ASSIGN":
            return self.parse_assignment()

        return self.parse_pipeline()

    def parse_block(self):

        self.advance()

        name = self.peek().value
        self.advance()

        self.advance()

        pipe = self.parse_pipeline()

        self.advance()

        return BlockDef(name, pipe)

    def parse_assignment(self):

        name = self.peek().value
        self.advance()

        self.advance()

        pipe = self.parse_pipeline()

        return Assignment(name, pipe)

    def parse_pipeline(self):

        start = None
        ops = []

        while self.pos < len(self.tokens):

            tok = self.peek()

            if tok.type == "NUMBER":
                start = tok.value
                self.advance()

            elif tok.type == "IDENT":

                if tok.value == "range":

                    self.advance()

                    a = self.peek().value
                    self.advance()

                    b = self.peek().value
                    self.advance()

                    start = list(range(a, b+1))

                else:
                    start = tok.value
                    self.advance()

            elif tok.type == "PIPE":

                self.advance()

                name = self.peek().value
                self.advance()

                args = []

                while self.peek().type not in ["PIPE", "EOL"]:
                    args.append(self.peek().value)
                    self.advance()

                ops.append(Operation(name, args))

            elif tok.type == "EOL":
                self.advance()

                if start is not None:
                    break

        return Pipeline(start, ops)

