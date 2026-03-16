
from parse_value import parse_value,variables
from execute_pipeline import execute_pipeline
from engine import run


# -----------------------------
# REPL
# -----------------------------

def repl():

    print("NovaPipe Phase4")
    print("exit to quit")

    while True:

        line = input("NovaPipe > ")

        if line == "exit":
            break

        try:
            run(line)
        except Exception as e:
            print("Error:", e)

