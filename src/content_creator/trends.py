from __future__ import annotations

import random
from dataclasses import dataclass
from typing import List


@dataclass
class Trend:
    keyword: str
    description: str


def get_regional_trends(region: str) -> List[Trend]:
    regional_trends = {
        "uganda": [
            Trend("kampala vibes", "city nightlife moments"),
            Trend("kisoboka", "it is possible optimism"),
            Trend("matooke love", "local comfort food pride"),
        ],
        "kenya": [
            Trend("maisha hustle", "daily grind motivation"),
            Trend("swahili flare", "kiswahili pop culture"),
            Trend("nai sundowner", "evening hangouts in nairobi"),
        ],
        "united states": [
            Trend("fall fits", "seasonal fashion inspiration"),
            Trend("game day", "sports fandom energy"),
            Trend("meal prep", "healthy convenience"),
        ],
    }

    default_trends = [
        Trend("local pride", "community shoutouts"),
        Trend("creator spotlight", "celebrating makers"),
        Trend("weekend plans", "relatable downtime"),
    ]

    key = region.lower()
    trends = regional_trends.get(key, default_trends)
    random.shuffle(trends)
    return trends
