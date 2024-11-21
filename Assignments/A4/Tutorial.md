This tutorial breaks down our Python code step-by-step, explaining how each part works. 

Step 1: Restart and Import Required Libraries
First, the code initializes the environment and imports necessary libraries:

ifcopenshell: For working with IFC models.

bonsai.bim.ifc: For accessing the loaded IFC file.

print("RESTART CODE")

import ifcopenshell  
from bonsai.bim.ifc import IfcStore  

# Load the IFC model
model = IfcStore.get_file()  
Step 2: Wall Volume Calculation
This section calculates the total volume of concrete walls.

Retrieve all walls in the model:


walls = model.by_type("IfcWall") 
total_volume_wall = 0  # Initialize total volume
Loop through each wall and extract its:

Name/Reference to check if it's made of concrete.
Area from its property sets.
Thickness from material layers.
Calculate the volume of concrete walls:


for entity in walls: 
    wall_thickness = None 
    wall_area = None 
    wallName = None 

    # Retrieve wall properties for name and area 
    for relDefinesByProperties in entity.IsDefinedBy: 
        if relDefinesByProperties.is_a("IfcRelDefinesByProperties"): 
            if relDefinesByProperties.RelatingPropertyDefinition.is_a("IfcPropertySet"): 
                for prop in relDefinesByProperties.RelatingPropertyDefinition.HasProperties: 
                    if prop.Name == 'Reference': 
                        wallName = prop.NominalValue.wrappedValue if prop.NominalValue else None 
                    elif prop.Name == 'Area': 
                        wall_area = prop.NominalValue.wrappedValue if prop.NominalValue else None 

    # Retrieve the wall thickness 
    material_associations = entity.HasAssociations 
    if material_associations: 
        for association in material_associations: 
            if association.is_a("IfcRelAssociatesMaterial"): 
                material = association.RelatingMaterial 
                if material.is_a("IfcMaterialLayerSetUsage") or material.is_a("IfcMaterialLayerSet"): 
                    for layer in material.MaterialLayers: 
                        wall_thickness = layer.LayerThickness / 1000  # Convert mm to m 
                        break  

    # Calculate volume for concrete walls
    if wallName and "concrete" in wallName.lower() and wall_area and wall_thickness: 
        wall_volume = wall_area * wall_thickness 
        total_volume_wall += wall_volume  # Add to total volume
Print the total volume of concrete walls:


print(f"Total volume of concrete walls: {total_volume_wall:.3f} m³") 
Step 3: Slab Volume Calculation
This section calculates the total volume of concrete slabs.

Retrieve all slabs in the model:


slabs = model.by_type("IfcSlab") 
total_volume_slab = 0  # Initialize total volume
Loop through each slab and extract:

Name/Reference to check for concrete.
Area and Thickness.
Calculate the slab volume:


for entity in slabs: 
    slab_thickness = None 
    slab_area = None 
    slab_name = None 

    # Retrieve slab properties for name and area 
    for relDefinesByProperties in entity.IsDefinedBy: 
        if relDefinesByProperties.is_a("IfcRelDefinesByProperties"): 
            if relDefinesByProperties.RelatingPropertyDefinition.is_a("IfcPropertySet"): 
                for prop in relDefinesByProperties.RelatingPropertyDefinition.HasProperties: 
                    if prop.Name == 'Reference': 
                        slab_name = prop.NominalValue.wrappedValue if prop.NominalValue else None 
                    elif prop.Name == 'Area': 
                        slab_area = prop.NominalValue.wrappedValue if prop.NominalValue else None 

    # Retrieve the slab thickness 
    material_associations = entity.HasAssociations 
    if material_associations: 
        for association in material_associations: 
            if association.is_a("IfcRelAssociatesMaterial"): 
                material = association.RelatingMaterial 
                if material.is_a("IfcMaterialLayerSetUsage"): 
                    material_layer_set = material.ForLayerSet 
                    if material_layer_set: 
                        for layer in material_layer_set.MaterialLayers: 
                            slab_thickness = layer.LayerThickness / 1000  # Convert mm to m 
                            break  

    # Calculate volume for concrete slabs
    if slab_name and "concrete" in slab_name.lower() and slab_area and slab_thickness: 
        slab_volume = slab_area * slab_thickness 
        total_volume_slab += slab_volume  # Add to total volume
Print the total volume of concrete slabs:


print(f"Total volume of concrete slabs: {total_volume_slab:.3f} m³") 
Step 4: Column Volume Calculation
This section calculates the total volume of concrete columns.

Retrieve all columns in the model:


columns = model.by_type("IfcColumn") 
total_volume_column = 0  # Initialize total volume
Loop through each column and extract:

Name/Reference to check for concrete.
Volume directly from its property set.
Calculate column volume:


for entity in columns: 
    column_name = None 
    column_volume = None 

    # Retrieve column properties for name and volume 
    for relDefinesByProperties in entity.IsDefinedBy: 
        if relDefinesByProperties.is_a("IfcRelDefinesByProperties"): 
            if relDefinesByProperties.RelatingPropertyDefinition.is_a("IfcPropertySet"): 
                for prop in relDefinesByProperties.RelatingPropertyDefinition.HasProperties: 
                    if prop.Name == 'Reference': 
                        column_name = prop.NominalValue.wrappedValue if prop.NominalValue else None 
                    elif prop.Name == 'Volume': 
                        column_volume = prop.NominalValue.wrappedValue if prop.NominalValue else None 

    # Add volume for concrete columns
    if column_name and "concrete" in column_name.lower() and column_volume: 
        total_volume_column += column_volume
Print the total volume of concrete columns:


print(f"Total volume of concrete columns: {total_volume_column:.3f} m³") 
Step 5: Gross Floor Area (GFA) Calculation
This section calculates the GFA of slabs above ground level.

Retrieve slabs and initialize variables:


slabs = model.by_type("IfcSlab") 
total_area_slab = 0  # Initialize total area
Loop through each slab, extracting:

Area.
Elevation (Z-coordinate).
Add areas of slabs above ground:


for entity in slabs: 
    slab_area = None 
    slab_elevation = None 

    # Retrieve slab properties for area 
    for relDefinesByProperties in entity.IsDefinedBy: 
        if relDefinesByProperties.is_a("IfcRelDefinesByProperties"): 
            if relDefinesByProperties.RelatingPropertyDefinition.is_a("IfcPropertySet"): 
                for prop in relDefinesByProperties.RelatingPropertyDefinition.HasProperties: 
                    if prop.Name == 'Area': 
                        slab_area = prop.NominalValue.wrappedValue if prop.NominalValue else None 

    # Retrieve elevation
    if entity.ObjectPlacement: 
        placement = entity.ObjectPlacement 
        if placement.is_a("IfcLocalPlacement"): 
            relative_placement = placement.RelativePlacement 
            if relative_placement and relative_placement.is_a("IfcAxis2Placement3D"): 
                if relative_placement.Location: 
                    slab_elevation = relative_placement.Location.Coordinates[2]  

    # Add area if above ground level
    if slab_elevation is not None and slab_elevation >= 0 and slab_area: 
        total_area_slab += slab_area
Print the total GFA:


print(f"GFA: {total_area_slab:.2f} m²") 
Step 6: Calculate CO₂ Footprint
Finally, calculate the CO₂ footprint based on the total volume of concrete and GFA.

Combine total concrete volume:


total_volume_concrete = total_volume_column + total_volume_slab + total_volume_wall
Calculate CO₂ footprint:


CO2_concrete = total_volume_concrete * 300 / (50 * total_area_slab)
print(f"Estimated CO2 footprint for concrete elements: {CO2_concrete:.2f} kg. CO2-eq./m²/yr") 
