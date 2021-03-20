import re
import typing
from typing import List, Mapping

all_items = [
    "Abyss Shriek",
    "Awoken Dream Nail",
    "City Crest",
    "Crystal Heart",
    "Cyclone Slash",
    "Dash Slash",
    "Descending Dark",
    "Desolate Dive",
    "Dream Gate",
    "Dream Nail",
    "Dreamer",
    "Elegant Key",
    "Great Slash",
    "Grimmchild",
    "Herrah",
    "Howling Wraiths",
    "Isma's Tear",
    "King's Brand",
    "Love Key",
    "Lumafly Lantern",
    "Lurien",
    "Mantis Claw",
    "Monarch Wings",
    "Monomon",
    "Mothwing Cloak",
    "Pale Ore-Basin",
    "Pale Ore-Colosseum",
    "Pale Ore-Crystal Peak",
    "Pale Ore-Grubs",
    "Pale Ore-Nosk",
    "Pale Ore-Seer",
    "Shade Cloak",
    "Shade Soul",
    "Shopkeeper's Key",
    "Simple Key-Basin",
    "Simple Key-City",
    "Simple Key-Lurker",
    "Simple Key-Sly",
    "Stag Nest Stag",
    "Tram Pass",
    "Vengeful Spirit",
]

all_items_secondary_mapping = {
    "Shade_Cloak": "Mothwing_Cloak",
    "Shade_Soul": "Vengeful_Spirit",
    "Descending_Dark": "Desolate_Dive",
    "Abyss_Shriek": "Howling_Wraiths",
    "Dream_Gate": "Dream_Nail",
    "Awoken_Dream_Nail": "Dream_Nail",
}


all_locations = [
    "Abyss",
    "Ancestral Mound",
    "Ancient Basin",
    "Beast's Den",
    "Black Egg Temple",
    "Blue Lake",
    "Cast Off Shell",
    "City of Tears",
    "Colosseum",
    "Crystal Peak",
    "Crystallized Mound",
    "Deepnest",
    "Dirtmouth",
    "Distant Village",
    "Failed Tramway",
    "Fog Canyon",
    "Forgotten Crossroads",
    "Fungal Core",
    "Fungal Wastes",
    "Greenpath",
    "Hallownest's Crown",
    "Hive",
    "Howling Cliffs",
    "Iselda",
    "Isma's Grove",
    "Junk Pit",
    "King's Pass",
    "King's Station",
    "Kingdom's Edge",
    "Lake of Unn",
    "Leg Eater",
    "Mantis Village",
    "Overgrown Mound",
    "Palace Grounds",
    "Pleasure House",
    "Queen's Gardens",
    "Queen's Station",
    "Resting Grounds",
    "Royal Waterways",
    "Salubra",
    "Sly (Key)",
    "Sly",
    "Soul Sanctum",
    "Spirit's Glade",
    "Stag Nest",
    "Stone Sanctuary",
    "Teacher's Archives",
    "Tower of Love",
    "Weaver's Den",
]

locations_secondary_mapping = {
    "Ancestral_Mound": "Forgotten_Crossroads",
    "Beasts_Den": "Deepnest",
    "Black_Egg_Temple": "Forgotten_Crossroads",
    "Blue_Lake": "Resting_Grounds",
    "Cast_Off_Shell": "Kingdoms_Edge",
    "Colosseum": "Kingdoms_Edge",
    "Crystallized_Mound": "Crystal_Peak",
    "Distant_Village": "Deepnest",
    "Failed_Tramway": "Deepnest",
    "Fungal_Core": "Fungal_Wastes",
    "Hallownests_Crown": "Crystal_Peak",
    "Howling_Cliffs": "Howling_Cliffs",
    "Iselda": "Dirtmouth",
    "Ismas_Grove": "Royal_Waterways",
    "Junk_Pit": "Royal_Waterways",
    "Kings_Pass": "Dirtmouth",
    "Kings_Station": "City_of_Tears",
    "Lake_of_Unn": "Greenpath",
    "Leg_Eater": "Fungal_Wastes",
    "Mantis_Village": "Fungal_Wastes",
    "Overgrown_Mound": "Fog_Canyon",
    "Palace_Grounds": "Ancient_Basin",
    "Pleasure_House": "City_of_Tears",
    "Queens_Station": "Fungal_Wastes",
    "Salubra": "Forgotten_Crossroads",
    "Sly_(Key)": "Dirtmouth",
    "Sly": "Dirtmouth",
    "Soul_Sanctum": "City_of_Tears",
    "Spirits_Glade": "Resting_Grounds",
    "Stag_Nest": "Howling_Cliffs",
    "Stone_Sanctuary": "Greenpath",
    "Teachers_Archives": "Fog_Canyon",
    "Tower_of_Love": "City_of_Tears",
    "Weavers_Den": "Deepnest",
}


def standardize_names(s: List[str], secondary_mapping: Mapping[str, str] = None):
    """ Standardizes names of HK things, then applies an optional secondary mapping.
        The secondary mapping is usually used if an item must be represented by the
        base item, or a location must be represented by a more general location.
    """

    orig_s = s.copy()
    patterns = [
        ("-.+", ""),  # remove everything after a dash
        (" ", "_"),  # replace spaces with underscores
        ("'", ""),  # remove apostrophes
    ]

    for pattern in patterns:
        s = list(map(lambda x: re.sub(pattern[0], pattern[1], x), s))
    mapping = dict(zip(orig_s, s))

    if secondary_mapping:  # If a new val exists, use that; otherwise, use old v.
        mapping = {k: secondary_mapping.get(v, v) for k, v in mapping.items()}

    return mapping


standardized_items = standardize_names(
    all_items, secondary_mapping=all_items_secondary_mapping
)
standardized_locations = standardize_names(
    all_locations, secondary_mapping=locations_secondary_mapping
)
