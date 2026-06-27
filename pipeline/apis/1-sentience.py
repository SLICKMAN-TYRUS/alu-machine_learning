#!/usr/bin/env python3
"""Module to find home planets of all sentient species using the SWAPI."""
import requests


def sentientPlanets():
    """Return list of home planet names of all sentient species.

    Fetches all species from the SWAPI, filters for those classified
    as 'sentient' or with a 'sentient' designation, then resolves
    each species' homeworld URL to its planet name.

    Returns:
        list: Names of home planets of sentient species.
    """
    planets = []
    url = "https://swapi.dev/api/species/"

    while url:
        response = requests.get(url)
        data = response.json()

        for species in data.get("results", []):
            classification = species.get("classification", "").lower()
            designation = species.get("designation", "").lower()

            if "sentient" in classification or "sentient" in designation:
                homeworld_url = species.get("homeworld")
                if homeworld_url:
                    planet_response = requests.get(homeworld_url)
                    planet_data = planet_response.json()
                    planets.append(planet_data.get("name"))

        url = data.get("next")

    return planets
