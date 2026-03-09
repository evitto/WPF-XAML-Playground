from Autodesk.Revit.DB import *

uidoc = __revit__.ActiveUIDocument
doc = uidoc.Document

columns = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_StructuralColumns).WhereElementIsElementType().ToElements()
levels = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Levels).WhereElementIsNotElementType().ToElements()

for level in levels:
    elevation = level.get_Parameter(BuiltInParameter.LEVEL_ELEV).AsDouble()
    if elevation == 3000/304.8:
        level_0 = level
for column in columns:
    column_name = column.get_Parameter(BuiltInParameter.SYMBOL_NAME_PARAM).AsString()
    if column_name == '450x600':
        column_type = column

t = Transaction(doc,"Column")
t.Start()
col = doc.Create.NewFamilyInstance(XYZ(0,0,0),column_type,level_0,StructuralType.Column)
t.Commit()