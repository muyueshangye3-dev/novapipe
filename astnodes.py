
# -----------------------------
# AST
# -----------------------------

class Pipeline:
    def __init__(self, start, ops):
        self.start = start
        self.ops = ops


class Operation:
    def __init__(self, name, args):
        self.name = name
        self.args = args


class Assignment:
    def __init__(self, name, pipe):
        self.name = name
        self.pipe = pipe


class BlockDef:
    def __init__(self, name, pipe):
        self.name = name
        self.pipe = pipe

