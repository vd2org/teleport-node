import json
import sys

import requests


def get_releases(repo: str, limit: int = 10, final_only: bool = False) -> set[str]:
    releases = requests.get(f"https://api.github.com/repos/{repo}/releases?per_page={limit}").json()

    if not isinstance(releases, list):
        return set()

    if final_only:
        releases = (release for release in releases if not (release.get("prerelease") or release.get("draft")))

    return set(release["tag_name"] for release in releases)


def run(my_repo: str, foreign_repo: str) -> tuple[str, ...]:
    foreign_releases = get_releases(foreign_repo, 10, final_only=True)
    my_releases = get_releases(my_repo, 100)

    return tuple(sorted(foreign_releases - my_releases))


def main():
    try:
        my_repo, foreign_repo = sys.argv[1:]
    except ValueError:
        print(f"Usage: python {sys.argv[0]} <my_repo> <foreign_repo>", file=sys.stderr)
        sys.exit(-1)

    versions = run(my_repo, foreign_repo)

    encoded = json.dumps(versions, separators=(",", ":"))

    print(encoded, flush=True)


if __name__ == '__main__':
    main()
