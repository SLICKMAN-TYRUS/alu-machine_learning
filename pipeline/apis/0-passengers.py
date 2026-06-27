#!/usr/bin/env python3
"""Module to find available starships by passenger capacity using the SWAPI."""
import requests


def availableShips(passengerCount):
    """Return list of ships that can hold at least passengerCount passengers.

    Args:
        passengerCount (int): Minimum number of passengers the ship must hold.

    Returns:
        list: Names of ships that meet the passenger requirement,
              or an empty list if none are found.
    """
    ships = []
    url = "https://swapi.dev/api/starships/"

    while url:
        response = requests.get(url)
        data = response.json()

        for ship in data.get("results", []):
            passengers = ship.get("passengers", "0")
            passengers = passengers.replace(",", "").replace(".", "")
            try:
                if int(passengers) >= passengerCount:
                    ships.append(ship["name"])
            except (ValueError, TypeError):
                pass

        url = data.get("next")

    return ships
