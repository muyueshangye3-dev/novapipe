class VM:

    def __init__(self):
        self.stack = []

    def run(self, code):

        for instr, arg in code:

            if instr == "PUSH":
                self.stack.append(arg)

            elif instr == "ADD":
                v = self.stack.pop()
                self.stack.append(v + arg)

            elif instr == "MUL":
                v = self.stack.pop()
                self.stack.append(v * arg)

            elif instr == "PRINT":
                print(self.stack[-1])
