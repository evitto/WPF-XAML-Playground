import clr

clr.AddReference("RevitAPI")
from Autodesk.Revit.DB import *

# List everything inside Autodesk.Revit.DB
print(dir())