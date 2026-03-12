from pyrevit import revit, forms
from Autodesk.Revit.DB import *
from Autodesk.Revit.UI.Selection import ObjectType

doc = revit.doc
uidoc = revit.uidoc
view = uidoc.ActiveView

# Pick edges
selected_refs = uidoc.Selection.PickObjects(ObjectType.Edge, "Select edges to modify")

if not selected_refs:
    forms.alert("No edges selected.")
else:
    # Get first available line pattern
    line_patterns = FilteredElementCollector(doc).OfClass(LinePatternElement).ToElements()
    if not line_patterns:
        forms.alert("No line patterns found in document.")
    else:
        line_pattern = line_patterns[0]

        t = Transaction(doc, "Modify Linework")
        t.Start()
        try:
            for edge_ref in selected_refs:
                # Get the element the edge belongs to
                elem = doc.GetElement(edge_ref.ElementId)

                # Build override settings with the new line pattern
                ogs = OverrideGraphicSettings()
                ogs.SetProjectionLinePatternId(line_pattern.Id)

                # Apply the override to the element in the active view
                view.SetElementOverrides(elem.Id, ogs)

            t.Commit()
            forms.alert("Modified {} edges using line pattern '{}'.".format(
                len(selected_refs), line_pattern.Name))

        except Exception as e:
            if t.HasStarted() and not t.HasEnded():
                t.RollbackToSavepoint()  # fallback
                t.RollBack()
            forms.alert("Error: {}".format(str(e)))