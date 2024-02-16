{
    "name": "Harvest Hub",
    "depends": ["base", "mail"],
    "author": "jatin",
    "installable": True,
    "data": [
        "security/ir.model.access.csv",
        "data/sequence.xml",
        "views/harvest_farmer_views.xml",
        "views/harvest_location_views.xml",
        "views/harvest_animal_views.xml",
        "views/harvest_menu.xml",
    ],
    "application": True,
}
