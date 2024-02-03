import sys


def bump_version(file_name: str, old_version: str, new_version: str):
    with open(file_name, 'r') as file:
        contents = file.read()

    contents = contents.replace(old_version, new_version)

    with open(file_name, 'w') as file:
        file.write(contents)


def main():
    try:
        file_name, old_version, new_version = sys.argv[1:]
    except ValueError:
        print(f"Usage: python {sys.argv[0]} <file_name> <old_version> <new_version>")
        sys.exit(-1)

    try:
        bump_version(file_name, old_version, new_version)
    except (FileNotFoundError, IsADirectoryError):
        print(f"File not found: {file_name}", file=sys.stderr)
        sys.exit(-1)


if __name__ == '__main__':
    main()
