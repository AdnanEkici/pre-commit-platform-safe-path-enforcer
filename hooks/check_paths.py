#!/usr/bin/env python
import sys
import re

pattern = r'([\'"])[^*+{}()?|^$[\]\s]*[\\/][^*+{}()?|^$[\]\s]*\1'

exit_code = 0
for filename in sys.argv[1:]:
    with open(filename, 'r') as file:
        lines = file.readlines()

    for i, line in enumerate(lines, start=1):
        # Skip comment lines and lines with 'noqa'
        stripped_line = line.lstrip()
        if stripped_line.startswith('#') or 'noqa' in stripped_line:
            continue

        for match in re.finditer(pattern, line):
            print(f'ERROR in {filename}, line {i}: Detected possible file path "{match.group(0)}". Please use os.sep or os.path.join instead.')
            exit_code = 1

sys.exit(exit_code)