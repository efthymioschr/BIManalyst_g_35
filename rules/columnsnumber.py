import ifcopenshell
from bonsai.bim.ifc import IfcStore
file = IfcStore.get_file()
things = file.by_type('IfcColumn')
print("Num of columns:" , len(things))
  
