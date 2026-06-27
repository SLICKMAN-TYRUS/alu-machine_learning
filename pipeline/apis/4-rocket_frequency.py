#!/usr/bin/env python3
"""Script to display the number of SpaceX launches per rocket."""
import requests


if __name__ == '__main__':
    """Fetch all SpaceX launches and print launch counts per rocket.

    Results are ordered by launch count (descending), then alphabetically
    by rocket name for ties.
    """
    launches_response = requests.get("https://api.spacexdata.com/v4/launches")
    launches = launches_response.json()

    rocket_counts = {}
    for launch in launches:
        rocket_id = launch.get("rocket")
        rocket_counts[rocket_id] = rocket_counts.get(rocket_id, 0) + 1

    rockets_response = requests.get("https://api.spacexdata.com/v4/rockets")
    rockets = rockets_response.json()

    rocket_names = {rocket["id"]: rocket["name"] for rocket in rockets}

    results = [
        (rocket_names[rid], count)
        for rid, count in rocket_counts.items()
        if rid in rocket_names
    ]

    results.sort(key=lambda x: (-x[1], x[0]))

    for rocket_name, count in results:
        print("{}: {}".format(rocket_name, count))
