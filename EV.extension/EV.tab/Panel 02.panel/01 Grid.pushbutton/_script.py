from Autodesk.Revit.DB import *

uidoc = __revit__.ActiveUIDocument
doc = uidoc.Document

p1 = XYZ(0,0,0)
p2 = XYZ(50,0,0)
line = Line.CreateBound(p1,p2)


t = Transaction(doc, 'Grid Create')
t.Start()
grid = Grid.Create(doc,line)
grdname = grid.get_Parameter(BuiltInParameter.DATUM_TEXT)
grdname.Set("X")
t.Commit()