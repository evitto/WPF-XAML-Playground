from Autodesk.Revit.DB import *
from Autodesk.Revit.UI.Selection import Selection

uidoc = __revit__.ActiveUIDocument
doc = __revit__.ActiveUIDocument.Document
selection = uidoc.Selection

Sel_Obj = selection.GetElementIds()
Elements = [doc.GetElement(i) for i in Sel_Obj]

result = []

for i in Elements:
    result.append(i.Name)

for i in result:
    print(i)