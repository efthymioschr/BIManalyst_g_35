import ifcopenshell
from bonsai.bim.ifc import IfcStore
file = IfcStore.get_file()
things = file.by_type('Ifcwall')
print("Num of walls:" , len(things))
