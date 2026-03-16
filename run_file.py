from execute_pipeline import execute_pipeline
from engine import run


# ----------------------------- 
# FILE RUN
# -----------------------------

def run_file(file):

    with open(file) as f:
        code = f.read()

    for block in code.split("\n\n"):
        run(block)
