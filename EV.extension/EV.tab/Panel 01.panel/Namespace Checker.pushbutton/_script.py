# ----------------------------
# Revit API Namespace Explorer
# ----------------------------

import clr
import inspect

# Add references
clr.AddReference("RevitAPI")
clr.AddReference("RevitAPIUI")

# Import namespaces
import Autodesk.Revit.DB as db
import Autodesk.Revit.UI as ui

def list_namespace(namespace, name=""):
    """
    Prints all classes and sub-namespaces in a namespace as a list
    """
    print("Namespace:", name or namespace.__name__)
    items = []

    for n, obj in inspect.getmembers(namespace):
        if inspect.isclass(obj):
            items.append(n)
        elif inspect.ismodule(obj):  # sub-namespace
            items.append(n + " (sub-namespace)")

    # Print as a numbered list
    for i, item in enumerate(items, start=1):
        print("{}. {}".format(i, item))
    print("\n" + "-"*40 + "\n")

# Explore Autodesk.Revit.DB
list_namespace(db, "Autodesk.Revit.DB")

# Explore Autodesk.Revit.UI
list_namespace(ui, "Autodesk.Revit.UI")