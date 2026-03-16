from token import tokenize
from executor import Executor
from parser import Parser

# -----------------------------
# ENGINE
# -----------------------------

executor = Executor()

def run(code):

    tokens = tokenize(code)

    parser = Parser(tokens)

    node = parser.parse()

    executor.execute(node)
