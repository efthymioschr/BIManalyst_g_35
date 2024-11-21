Group 35  

Focus Area: Sustainability & Materials 

We are verifying that the IFC model contains a specified number of columns (IfcColumn) as indicated in the provided building design.  Even though the number of the columns is not specified in any of the reports we received we calculated the number from the floor plans we found in the architectural report under the name CES_BLD_24_06_ARC in pages 34, 35 and 36. As we saw from the floor plans we have 40 columns on each floor.  We have 17 upper ground floor and 2 underground floors and after the calculation we found that we have a total of 40*1=760 columns plus the four columns two on each level of the basement to support the ramp we have in total 760+4=764 columns. 

Script Overview: 
The Python script we developed focuses on analyzing an Industry Foundation Classes (IFC) file, specifically to determine the number of columns present in the building model. We used the ifcopenshell library and the bonsai.bim.ifc module to interact with the IFC file, extract structural data, and verify the number of IfcColumn elements. 

Script Functionality: 
The script’s primary purpose is to verify the claim that a given IFC model contains a certain number of columns by comparing the expected number from the report to the actual number found in the model. 


Sample code:  

import ifcopenshell 
from bonsai.bim.ifc import IfcStore 
file = IfcStore.get_file() 
things = file.by_type('IfcColumn') 
print("Num of columns:" , len(things)) 

In conclusion to verify the number of the columns we ran the above Python script, and it returned a total of 764 columns, which matches our initial calculations based on the architectural report. 

This confirmation indicates that the column count in the IFC model is accurate and aligns with the floor plans, supporting the structural integrity of the design as indicated in the building's architectural report. 

 

 

 

 
