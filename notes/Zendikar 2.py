raven_gorge_map = {
    "Spawn Point": {
        "NAME": "Spawn Point",
        "DESCRIPTION": "Test room",
        "PATHS": {
            "North": "Raven Gorge"
        }
    },
    "Raven Gorge 1": {
        "NAME": "Raven Gorge 1",
        "DESCRIPTION": "Nothing",
        "PATHS": {
            "South": "Spawn Point",
            "North": "Raven Gorge 2"
        }
    },
    "Raven Gorge 2": {
        "NAME": "Raven Gorge 2",
        "DESCRIPTION": "Eldrazi Scout",
        "PATHS": {
            "South": "Raven Gorge 1",
            "North": "Raven Gorge 3",
            "West": "Raven Gorge 2 Left"
        }
    },
    "Raven Gorge 2 Left": {
      "NAME": "Raven Gorge 2 Left",
      "DESCRIPTION": "25 Gold",
      "PATHS": {
            "East": "Raven Gorge 2"
        }
    },
    "Raven Gorge 3": {
        "NAME": "Raven Gorge 3",
        "DESCRIPTION": "Eldrazi Scion",
        "PATHS": {
            "East": "Raven Gorge 3 Right",
            "North": "Raven Gorge 4",
            "South": "Raven Gorge 2"
        }
    },
    "Raven Gorge 3 Right": {
        "NAME": "Raven Gorge 3 Right",
        "DESCRIPTION": "Eldrazi Devastator",
        "PATHS": {
            "West": "Raven Gorge 3"
        }
    },
    "Raven Gorge 4": {
        "NAME": "Raven Gorge 4",
        "DESCRIPTION": "Shop",
        "PATHS": {
            "Spawn Point Sheltered Valley"
        }
    }
}

sheltered_valley_map = {
    "Spawn Point Sheltered Valley": {
        "NAME": "Spawn Point Sheltered Valley",
        "DESCRIPTION": "Spawn Point",
        "PATHS": {
            "West": "Sheltered Valley 1",
            "East": "Sheltered Valley 4"
        }
    },
    "Sheltered Valley 1": {
        "NAME": "Sheltered Valley 1",
        "DESCRIPTION": "Spawn Point",
        "PATHS": {
            "South": "Sheltered Valley 7",
            "North": "Sheltered Valley 2"
        }
    },
    "Sheltered Valley 2": {
        "NAME": "Sheltered Valley 2",
        "DESCRIPTION": "Dead body with 50 gold",
        "PATHS": {
            "South": "Sheltered Valley 1",
            "North": "Sheltered Valley 3"
        }
    },
    "Sheltered Valley 3": {
        "NAME": "Sheltered Valley 3",
        "DESCRIPTION": "Stream",
        "PATHS": {
            "South": "Sheltered Valley 2",
            "North": "Mountain"
        }
    },
    "Mountain": {
        "NAME": "Mountain",
        "DESCRIPTION": "Mountain",
        "PATHS": {
            "Spawn Point Mountain"
        }
    },
    "Sheltered Valley 7": {
        "NAME": "Sheltered Valley 7",
        "DESCRIPTION": "Strange Noise",
        "PATHS": {
            "South": "Sheltered Valley 8"
        }
    },
    "Sheltered Valley 8": {
        "NAME": "Sheltered Valley 8",
        "DESCRIPTION": "Making a fire",
        "PATHS": {
            "South": "Great Desert",
            "North": "Sheltered Valley 7"
        }
    },
    "Desert": {
        "NAME": "Desert",
        "DESCRIPTION": "Desert",
        "PATHS": {
            "Spawn Point Desert"
        }
    },
    "Sheltered Valley 4": {
        "NAME": "Sheltered Valley 4",
        "DESCRIPTION": "Mass of trees",
        "PATHS": {
            "North": "Sheltered Valley 5",
            "East": "Sheltered Valley 6"
        }
    },
    "Sheltered Valley 5": {
        "NAME": "Sheltered Valley 5",
        "DESCRIPTION": "Heavy canopy",
        "PATHS": {
            "North": "Lake",
            "South": "Sheltered Valley 4"
        }
    },
    "Lake": {
        "NAME": "Lake",
        "DESCRIPTION": "Lake",
        "PATHS": {
            "Spawn Point Lake"
        }
    },
    "Sheltered Valley 6": {
        "NAME": "Sheltered Valley 6",
        "DESCRIPTION": "Cabin, instant death",
        "PATHS": {}
        # None
    }
}
