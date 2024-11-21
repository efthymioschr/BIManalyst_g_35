TEAM : 35  

Efthymios Christodoulakis s232464 

Frederikke Secher Mosbech s183131 

 

A2a: About Group 

In team 35 we agreed that both of us are on level 1 of knowledge of Python code and we gain o total score of 2. 	 

Efthymios : level 1 (never coded before) 

Frederikke: level 1 (never coded before) 

 

A2b IDENTIFY CLAIM 

We choose to work with Building #2406 and initially reviewed all the subject reports. We wanted to focus on environmental sustainability and found the buildings CO2 footprint to be very interesting.  

The claim is included in the client report among the building BEATS on page 4. Here, it is stated that the CO2 footprint is 6,74 kg CO2-eq./m2/yr. As the LCA calculations are very extensive and our coding skills are very limited we want to focus on one of the main contributors in terms of materials, concrete. 

By creating a code that calculates the consumption of concrete in the building it is possible to estimate the main contributor to the LCA calculation and thereby check if the result of 6,74 6,74 kg CO2-eq./m2/yr is reasonable. 

 

A2c  USE CASE 

Checking the CO2 Footprint Claim:  To verify the claim, we would start by reviewing the IFC file (Industry Foundation Classes file) to extract the amount of concrete used in the building. The data from this file will allow us to identify the number and dimensions of concrete columns, which can then be used to calculate their volume. Once we know the total volume of concrete, we can calculate the CO2 contribution using the appropriate LCA Byg database conversion factors. 

For example, by determining the height and cross-sectional area of each column, we can estimate the concrete volume and then apply the relevant CO2 emission factors to compute the CO2-eq. per unit of concrete used. 

When would this claim need to be checked?: The CO2 footprint is assessed during the design phase to meet building regulations and ensure sustainability. The claim must be verified throughout the design process, especially when submitting the design to authorities, ensuring the office building stays below the 12 kg CO2 eq./m²/yr limit. 

 

Information Required for This Claim: 

Material specifications, particularly the amount and type of concrete used in the structure. 

Dimensions of structural elements (e.g., concrete columns, slabs, and beams). 

CO2 emission factors for the materials used, typically sourced from LCA Byg or other LCA tools. 

Building GFA for calculating the LCA with the unit of kg. CO2 eq. /m2/year. 

Relevant Phase for Checking the Claim: This claim falls within the design phase of the project. It is during this phase that decisions regarding material selection and structural design are made, which will directly influence the environmental footprint of the building. 

BIM Purpose Required for the Claim: For this analysis, the BIM (Building Information Model) serves the purpose of analyzing and communicating the material usage and environmental impact. Specifically, the structural model within the BIM environment is crucial, as it contains detailed information about the materials (e.g., concrete) used in the building’s structure. This model will help identify the quantities needed for CO2 footprint calculations. 

Review use case examples - do any of these help?, What BIM use case is this closest to? If you cannot find one from the examples, you can make a new one. 

Produce a BPMN drawing for your chosen use case. link to this so we can see it in your markdown file. To do this you will have to save it as an SVG, please also save the BPMN with it.mYou can use this online tool to create a BPMN file. 

 

A2d: SCOPE THE USE CASE 

In this part, we are tasked with identifying where a new script, function, or tool is required to enhance the analysis process in our project. The goal is to effectively calculate the CO2 footprint of the building by focusing on key structural elements such as columns, beams, core walls, foundations, and decks. Based on the ‘whole use case,’ we have identified specific areas where new components need to be developed. These components are highlighted below and are represented clearly in the accompanying BPMN diagram. 

New Scripts: 

We propose developing scripts that will extract detailed information from the building's IFC file. These scripts should automate the identification and quantification of specific building elements, including: 

Columns: A script to extract the number and dimensions of all columns (height, width, and length). 

Beams: A script to determine the number and dimensions of the beams. 

Core Walls: A script to identify the number and dimensions of core walls. 

Foundation: A script to assess the volume and dimensions of the foundation. 

Decks: A script to measure the total area of floor decks. 

These scripts will streamline the process of collecting material data, which is essential for calculating the total CO2 footprint based on the materials used. 

 

New Functions: 

In addition to the scripts, several new functions are required to perform basic calculations on the extracted data: 

Count Function: A function that counts the total number of elements (e.g., columns, beams) from the IFC data. 

Area Measurement Function: A function to measure the surface area of elements such as walls, decks, or beams. 

Height/Length Measurement Function: A function that calculates the height and length of structural elements such as columns and walls. 

Multiplication Function: A function to multiply dimensions (e.g., height × width × depth) to obtain the total volume of elements. 

Addition Function: A function that sums up the total material quantities (e.g., total concrete volume from all structural elements). 

These functions will provide the foundation for calculating the amount of material used and, subsequently, the environmental impact (e.g., CO2 emissions). 

 

New Tool: 

We also propose the development of a new tool that will integrate the aforementioned scripts and functions. This tool will: 

Generate the total material volume: Specifically, the tool will extract and compute the total volume (in cubic meters) of a specific material, such as concrete, directly from the IFC file. 

This tool will allow users to select specific material types and automatically calculate the volume for each, ensuring accuracy in estimating the building’s CO2 footprint. 

Scope of Use Case 

The new scripts, functions, and tools will work together to: 

Extract data from the IFC file. 

Perform calculations on the data (such as volume, area, and height measurements). 

Generate a report on the total amount of material used, specifically focusing on the structural materials that contribute to the building’s CO2 footprint. 

The introduction of these components will significantly improve the accuracy and efficiency of the CO2 calculation process by automating data extraction and computation. 
 

A2e: TOOL IDEA 

The purpose of our tool is to calculate the amount of concrete in the building based on only the file path to an IFC of the structural model. If possible, the results should be converted into a file that can be read by LCAbyg. 

The tool can be useful in the early design stages to be used by structural engineers and architects as an indication of the CO2 footprint of the building. By having the indication, it is easier to comply with building codes in the later stages of the process. This tool is increasingly relevant as the LCA requirements are being adapted yearly from 2025. 

A2f: INFORMATION REQUIREMENTS 

We need to extract the following elements and their dimensions from the IFC file: 

Columns = ifcColumn/square Column:STR – Concrete Column – 600x600mm 

Columns = ifcColumn/square Column:STR – Concrete Column – 480x480mm 

Beams = ifcBeam/Intermediate beam (D):STR – Intermediate Deltabeam 293 

Beams = ifcBeam/ Edge beam (DR):STR – Edge Deltabeam – DR22-250 

Core walls = ifcWall/Basic:STR 

Foundation = ifcSlab - mat foundation 

Decks = ifcSlab/floor 

Basement wall = ifcWall/Basic wall:GEO 

It would be nice to separate different sizes of collums and beams from eachother when calling them in ifcXXX without defining their entire name. We would need read about how to do this. 

This information is located within the structural model of the IFC file, which includes the necessary details about the building's structural elements (e.g., columns, beams, walls, slabs).  

These information are present in the structural model of the IFC file. Each structural element (e.g., columns, beams, walls) is associated with an IFC class (e.g., ifcColumn, ifcBeam, ifcWall, ifcSlab). 

Plan for Learning 

To address these needs, we will need to: 

Review IFC documentation to fully understand the structure of ifcColumn, ifcBeam, ifcWall, and ifcSlab classes. 

Experiment with filtering techniques in ifcOpenShell to identify and separate different sizes of columns, beams, and other structural elements. 

Collaborate with peers on improving Python scripting within ifcOpenShell for efficient data extraction. 

A2g: Software 

We haven't decided on the software license yet, but it will be announced later in the project. 

 
