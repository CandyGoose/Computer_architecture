import json
import os
import sys

from machine.cpu import DataPath, ControlUnit


def start(code_file, instructions, input_tokens, memory_capacity):
    data_path = DataPath(memory_capacity, input_tokens)
    cu = ControlUnit(code_file, instructions, data_path)
    result = cu.execute()
    cu.log.close()
    return result


def get_tokens(input_file):
    with open(input_file, "r", encoding="utf-8") as f:
        input_string = f.readline()

    input_tokens = []
    match os.path.basename(input_file):
        case "hello_user_name.txt":
            time = 8157
            offset = 100
        case _:
            time = 11
            offset = 100

    for char in input_string:
        input_tokens.append((time, char))
        time += offset
    input_tokens.append((time, "\x00"))
    return input_tokens


def main(code_file, input_file):
    input_tokens = get_tokens(input_file)
    with open(code_file, "r", encoding="utf-8") as f:
        code = json.load(f)

    output_chars, instr_count, tick_count = start(os.path.basename(code_file), code, input_tokens, 100)

    if len(output_chars) > 0:
        print("".join(output_chars))
    print(f"ticks_count: {tick_count}")
    print(f"instructions_count: {instr_count}")


if __name__ == "__main__":
    assert len(sys.argv) == 3, "Wrong arguments: cpu.py <code_file> <input_file>"
    _, code_file, input_file = sys.argv

    main(code_file, input_file)
