import ifcopenshell
def count_ifc_columns(model):
    columns = model.by_type('IfcColumn') 
    print("Num of columns:", len(columns))  
    return len(columns)
