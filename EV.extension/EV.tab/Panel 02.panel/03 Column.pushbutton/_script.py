from Autodesk.Revit.DB import *
from Autodesk.Revit.DB.Structure import StructuralType
doc = __revit__.ActiveUIDocument.Document


columnTypes = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_StructuralColumns).WhereElementIsElementType().ToElements()
levels = FilteredElementCollector(doc).OfClass(Level).ToElements()
symbol = columnTypes[4]
level = levels[0]


t = Transaction(doc, 'Column')
t.Start()
if not symbol.IsActive:
    symbol.Activate()
    doc.Regenerate()
cCol = doc.Create.NewFamilyInstance(XYZ(0,0,0),symbol,level,StructuralType.Column)
t.Commit()