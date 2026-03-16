import sys
from parse_value import parse_value,variables
from execute_pipeline import execute_pipeline
from run_file import run_file
from repl import repl


# -----------------------------
# MAIN
# -----------------------------

def main():

    if len(sys.argv) > 1:
        run_file(sys.argv[1])
    else:
        repl()


if __name__ == "__main__":
    main()