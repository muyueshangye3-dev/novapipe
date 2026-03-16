from astnodes import Assignment,BlockDef,Pipeline

# -----------------------------
# EXECUTOR
# -----------------------------

class Executor:

    def __init__(self):

        self.vars = {}
        self.blocks = {}

    def resolve(self, v):

        if isinstance(v, str) and v in self.vars:
            return self.vars[v]

        return v

    def run_pipe(self, pipe):

        value = self.resolve(pipe.start)

        for op in pipe.ops:

            name = op.name
            args = op.args

            if name == "add":

                n = int(args[0])

                if isinstance(value, list):
                    value = [v+n for v in value]
                else:
                    value += n

            elif name == "mul":

                n = int(args[0])

                if isinstance(value, list):
                    value = [v*n for v in value]
                else:
                    value *= n

            elif name == "map":

                op2 = args[0]
                n = int(args[1])

                if op2 == "mul":
                    value = [v*n for v in value]

                if op2 == "add":
                    value = [v+n for v in value]

            elif name == "filter":

                cond = args[0]
                n = int(args[1])

                if cond == "gt":
                    value = [v for v in value if v>n]

                if cond == "lt":
                    value = [v for v in value if v<n]

            elif name == "sum":
                value = sum(value)

            elif name == "count":
                value = len(value)

            elif name == "print":
                print(value)

            elif name in self.blocks:

                block = self.blocks[name]
                value = self.run_pipe(block)

        return value

    def execute(self, node):

        if isinstance(node, Assignment):

            v = self.run_pipe(node.pipe)

            self.vars[node.name] = v

        elif isinstance(node, BlockDef):

            self.blocks[node.name] = node.pipe

        elif isinstance(node, Pipeline):

            self.run_pipe(node)


