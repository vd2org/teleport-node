import sys

from packaging.version import parse, InvalidVersion


def main():
    try:
        version1, version2 = sys.argv[1:]
    except ValueError:
        print("Usage: python compare_version.py <version1> <version2>", file=sys.stderr)
        sys.exit(-1)

    try:
        version1, version2 = parse(version1), parse(version2)
    except InvalidVersion as e:
        print(e.args[0], file=sys.stderr)
        sys.exit(-1)

    if version1 < version2:
        print("gt")
    elif version1 > version2:
        print("lt")
    else:
        print("eq")


if __name__ == '__main__':
    main()
