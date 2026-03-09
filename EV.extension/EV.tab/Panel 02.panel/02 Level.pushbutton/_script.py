from Autodesk.Revit.DB import *

uidoc = __revit__.ActiveUIDocument
doc = uidoc.Document


t = Transaction(doc, "Level")
t.Start()
lvl = Level.Create(doc, 3000/304.8)
lvlname = lvl.get_Parameter(BuiltInParameter.DATUM_TEXT)
lvlname.Set('TEST LEVEL')
t.Commit()

print(lvlname.AsString())