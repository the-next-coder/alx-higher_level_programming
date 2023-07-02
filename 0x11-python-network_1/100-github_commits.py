#!/usr/bin/python3
"""
list 10 commits (from the most recent to oldest)
of the repository “rails” by the user “rails”
"""

import sys
import requests


def commit_list(repository, owner):
    """
    function to get list of commits
    """
    url = f"https://api.github.com/repos/{owner}/{repository}/commits"
    response = requests.get(url)

    if response.status_code == 200:
        commits = response.json()[:10]
        for commit in commits:
            sha = commit["sha"]
            author_name = commit["commit"]["author"]["name"]
            print(f"{sha}: {author_name}")


if __name__ == "__main__":
    repository = sys.argv[1]
    owner = sys.argv[2]
    commit_list(repository, owner)
