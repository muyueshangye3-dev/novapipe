
class Compiler:

    def compile(self, pipeline):

        code = []

        code.append(("PUSH", pipeline.start))

        for op in pipeline.ops:

            if op.name == "add":
                code.append(("ADD", int(op.args[0])))

            elif op.name == "mul":
                code.append(("MUL", int(op.args[0])))

            elif op.name == "print":
                code.append(("PRINT", None))

        return code
