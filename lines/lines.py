import sys
import os


def main():
    """Count the lines of code in a python file."""
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    else:
        if not sys.argv[1].endswith(".py"):
            sys.exit("Not a Python file")
        else:
            print(counter(sys.argv[1]))


def counter(file_py):

    """Count lines of code, include doc-strings.
    do not count blank space and comments lines """

    try:
        ignored_lines = 0

        with open(file_py, "r") as rows:
            # Get the total line-count.
            rows = list(enumerate(rows.readlines(), start=1))

            # Go over every line and see it counts as code.
            for line_number, lines in rows:
                if (lines.strip().startswith("#") or lines.strip().startswith("\n") or lines.isspace()):
                 ignored_lines = ignored_lines + 1

            return int(rows[-1][0]) - ignored_lines

    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()