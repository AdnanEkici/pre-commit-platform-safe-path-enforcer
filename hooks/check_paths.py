#!/usr/bin/env python
import sys
import re

def check_for_path_seperator(python_file = None):
    pattern = r'([\'"])(?!https?:\/\/)[^*+{}()?|^$[\]\s]*[\\\/][^*+{}()?|^$[\]\s]*\1'

    exit_code = 0

    if python_file is None:
        filenames = sys.argv[1:]
    else:
        filenames = [python_file]

    for filename in filenames:
        with open(filename, 'r') as file:
            lines = file.readlines()
        for i, line in enumerate(lines, start=1):
            # Skip comment lines and lines with 'noqa'
            stripped_line = line.lstrip()
            if stripped_line.startswith('#') or 'noqa' in stripped_line:
                continue

            for match in re.finditer(pattern, line):
                print(
                    f'ERROR in {filename}, line {i}: Detected possible file path "{match.group(0)}". Please use os.sep or os.path.join instead.')
                exit_code = 1


    return exit_code

if __name__ == '__main__':
    hook_exit_code = check_for_path_seperator()
    sys.exit(hook_exit_code)