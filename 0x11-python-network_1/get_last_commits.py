#!/usr/bin/python3
"""
Experiment with a way to print last 10 commits without
using a function
"""
import requests

if __name__ == "__main__":
    owner = "rails"
    repo = "rails"
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    parameters = {
        "sha": "main",
        "per_page": 10,
    }
    response = requests.get(url, params=parameters)
    if response.status_code == 200:
        commits = response.json()
        for commit in commits:
            sha = commit["sha"]
            author = commit["commit"]["author"]["name"]
            print(f"{sha}: {author}")
