import clr

clr.AddReference("RevitAPI")
clr.AddReference("RevitAPIUI")

from Autodesk.Revit.DB import *
from Autodesk.Revit.UI import *
from Autodesk.Revit.UI.Selection import *

# pyRevit provides UIApplication as __revit__
uiapp = __revit__
uidoc = uiapp.ActiveUIDocument
doc = uidoc.Document

# Collect all walls
walls = FilteredElementCollector(doc).OfClass(Wall).ToElements()

output = []

for wall in walls:
    param = wall.LookupParameter("Comments")
    if param:
        # Use .format() instead of f-string
        output.append("Wall ID {}: {}".format(wall.Id, param.AsString()))
    else:
        output.append("Wall ID {}: <No Comments>".format(wall.Id))

# Show results
TaskDialog.Show("Wall Comments", "\n".join(output))