#!/usr/bin/env python3
"""Script to display the next upcoming SpaceX launch using the SpaceX API."""
import requests


if __name__ == '__main__':
    """Fetch and print details of the next upcoming SpaceX launch.

    Output format:
    <launch name> (<date>) <rocket name> - <launchpad name> (<locality>)
    """
    launches_url = "https://api.spacexdata.com/v4/launches/upcoming"
    response = requests.get(launches_url)
    launches = response.json()

    upcoming = sorted(
        launches, key=lambda x: x.get("date_unix", float("inf"))
    )
    next_launch = upcoming[0]

    name = next_launch.get("name")
    date = next_launch.get("date_local")

    rocket_id = next_launch.get("rocket")
    rocket_response = requests.get(
        "https://api.spacexdata.com/v4/rockets/{}".format(rocket_id)
    )
    rocket_name = rocket_response.json().get("name")

    launchpad_id = next_launch.get("launchpad")
    launchpad_response = requests.get(
        "https://api.spacexdata.com/v4/launchpads/{}".format(launchpad_id)
    )
    launchpad_data = launchpad_response.json()
    launchpad_name = launchpad_data.get("name")
    launchpad_locality = launchpad_data.get("locality")

    print("{} ({}) {} - {} ({})".format(
        name, date, rocket_name, launchpad_name, launchpad_locality
    ))
