#!/usr/bin/env python3
"""Script to print the location of a GitHub user via the GitHub API."""
import requests
import sys
import time


if __name__ == '__main__':
    """Fetch and print the location of a GitHub user.

    Usage: ./2-user_location.py <github_api_url>
    Prints the user's location, 'Not found' if the user doesn't exist,
    or 'Reset in X min' if the rate limit has been exceeded.
    """
    url = sys.argv[1]
    response = requests.get(url)

    if response.status_code == 403:
        reset_time = int(response.headers.get("X-Ratelimit-Reset", 0))
        minutes = round((reset_time - time.time()) / 60)
        print("Reset in {} min".format(minutes))
    elif response.status_code == 404:
        print("Not found")
    else:
        data = response.json()
        print(data.get("location"))
