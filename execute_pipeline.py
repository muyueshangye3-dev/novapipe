import sys
from parse_value import parse_value,variables

# -------------------------
# パイプライン実行
# -------------------------

def execute_pipeline(lines):

    value = None

    for raw in lines:

        line = raw.strip()

        if not line:
            continue

        # 初期値
        if not line.startswith("|"):

            parts = line.split()

            if parts[0] == "range":

                start = int(parts[1])
                end = int(parts[2])

                value = list(range(start, end + 1))

            else:
                value = parse_value(line)

            continue

        # pipe operation
        cmd = line[1:].strip().split()

        op = cmd[0]

        # print
        if op == "print":
            print(value)

        # add
        elif op == "add":

            n = int(cmd[1])

            if isinstance(value, list):
                value = [v + n for v in value]
            else:
                value += n

        # mul
        elif op == "mul":

            n = int(cmd[1])

            if isinstance(value, list):
                value = [v * n for v in value]
            else:
                value *= n

        # map
        elif op == "map":

            operation = cmd[1]
            n = int(cmd[2])

            if operation == "mul":
                value = [v * n for v in value]

            elif operation == "add":
                value = [v + n for v in value]

        # filter
        elif op == "filter":

            cond = cmd[1]
            n = int(cmd[2])

            if cond == "gt":
                value = [v for v in value if v > n]

            elif cond == "lt":
                value = [v for v in value if v < n]

        # sum
        elif op == "sum":
            value = sum(value)

        # count
        elif op == "count":
            value = len(value)

        else:
            print("Unknown operation:", op)

    return value

