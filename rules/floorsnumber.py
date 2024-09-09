import ifcopenshell
from bonsai.bim.ifc import IfcStore
file = IfcStore.get_file()
things = file.by_type('Ifcslab')
print("Num of floors:" , len(things))
