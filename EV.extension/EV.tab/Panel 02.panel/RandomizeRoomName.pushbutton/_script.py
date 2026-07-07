# -*- coding: utf-8 -*-
__title__ = "Randomize\nRoom Names"
__author__ = "EV"

import random
import clr
clr.AddReference("RevitAPI")
from Autodesk.Revit.DB import FilteredElementCollector, BuiltInCategory, BuiltInParameter, Transaction
from pyrevit import revit

ROOM_NAMES = [
    "Living Room", "Bedroom", "Master Bedroom", "Kitchen", "Dining Room",
    "Bathroom", "Master Bathroom", "Powder Room", "Laundry Room", "Mudroom",
    "Home Office", "Study", "Library", "Family Room", "Den", "Foyer",
    "Entry Hall", "Hallway", "Corridor", "Pantry", "Walk-In Closet",
    "Utility Room", "Storage Room", "Garage", "Sunroom", "Gym",
    "Media Room", "Guest Room", "Nursery", "Playroom",
]

doc = revit.doc
rooms = [r for r in FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Rooms).WhereElementIsNotElementType() if r.Area > 0]

t = Transaction(doc, "Randomize Room Names")
t.Start()
for room in rooms:
    room.get_Parameter(BuiltInParameter.ROOM_NAME).Set(ROOM_NAMES[int(random.random() * len(ROOM_NAMES))])
t.Commit()