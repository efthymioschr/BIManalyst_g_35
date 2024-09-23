# BIManalyst group 35
Focus Area:Sustainability & Materials 
We are verifying that the IFC model contains a specified number of columns (IfcColumn) as indicated in the provided building design.  As we saw from the floor plans we have 40 columns on each floor.  We have 17 upper ground floor and 2 underground floors and after the calculation we found that we have a total of 40*1=760 columns plus the four columns two on each level of the basement to support the ramp we have in total 760+4=764 columns. 
The above informations were taken from the architectural report under the name CES_BLD_24_06_ARC in pages 34 to 36.
The functionality of the code is to import the necessary libraries to handle IFC files, retrieve the current IFC file using IfcStore.get_file(), extract all elements in the IFC file that are of type IfcColumn (representing columns in the building structure), count the number of columns found in the file and prints the result.
