# ----------------------------
# Replace Grid Curve (ScopeBox removed)
# ----------------------------

import clr
clr.AddReference("RevitAPI")
clr.AddReference("RevitAPIUI")

from Autodesk.Revit.DB import *
from Autodesk.Revit.UI import *
from Autodesk.Revit.UI.Selection import *

# Core objects
uiapp = __revit__
uidoc = uiapp.ActiveUIDocument
doc = uidoc.Document

# Pick grid
picked_ref = uidoc.Selection.PickObject(ObjectType.Element, "Select a grid to modify")
grid = doc.GetElement(picked_ref)

if not isinstance(grid, Grid):
    TaskDialog.Show("Error", "Selected element is not a Grid.")
    raise Exception("Not a Grid")

# Old curve
old_curve = grid.Curve
start = old_curve.GetEndPoint(0)
end = old_curve.GetEndPoint(1)

# Example: offset X by 5 feet
offset = 5.0
new_start = XYZ(start.X + offset, start.Y, start.Z)
new_end = XYZ(end.X + offset, end.Y, end.Z)
new_curve = Line.CreateBound(new_start, new_end)

# Save old name
grid_name = grid.Name

# Replace grid
t = Transaction(doc, "Replace Grid Curve")
t.Start()
doc.Delete(grid.Id)
new_grid = Grid.Create(doc, new_curve)
new_grid.Name = grid_name
t.Commit()

TaskDialog.Show("Done", "Grid curve replaced successfully!")